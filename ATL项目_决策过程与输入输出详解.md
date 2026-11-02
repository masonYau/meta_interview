# ATL 项目：决策过程、颗粒度与输入输出详解

更新日期：2026-11-02。适用场景：Meta IC5、偏产品经理职责的英文面试。

依据：本人补充的项目事实，以及 `D:/yhl_back/atl_aps_2021` 的静态代码分析。没有运行生产数据，没有修改项目源码。

## 1. 项目主线与本人贡献

**主线：从东莞向宁德推广时，原有日计划面对更大规模，需要重新划分决策层次。我增加主计划负责需求与产能分配，让日计划聚焦批次和机台搭配，再增加排程后校正模型处理换型等细节。我还设计了初始仅使用稀疏候选批次、按求解结果逐步增加候选并重新求解的迭代机制；同时解决输入可复现和 M6S 共享资源建模的问题。**

### 证据标记

- **[业务已确认]** 本人在对话中确认的历史事实、设计动机或现场结果。
- **[代码已确认]** 当前备份中直接可见的读取、变量、约束、目标、输出与调用。
- **[设计解释]** 对实现作用、取舍和风险的分析，不等于当时逐项讨论过所有备选方案。
- **[建议方法]** 面向未来的验证或改进方案，英文使用 would。

### 版本与职责边界

1. **原来只有日计划；主计划和排程后校正均由本人增加。** 增加主计划的触发点，是从东莞推广到规模更大的宁德工厂。算法团队负责算法，ATL IT 负责系统前后端；不因此声称本人开发全部应用系统或拥有全部产品预算。
2. **主计划完成后不经过 PC 审核，直接分布式运行日计划。** 这是本人确认的现场部署方式。当前备份的 Python 单入口内部按计划块顺序循环，不能用它独立证明分布式调度实现，也不能以此否定现场部署。
3. **主计划中保留一定产能折扣**，为下层细化留余量。上线半年期间，未出现因主计划分配错误导致的日计划欠交；代价是可能增加额外转型。折扣比例、校准方式、额外转型数量尚未补充。
4. **当前代码是 M6S 后续组合批次改进前的旧版本。** 旧版本已经有尽可能同开同收的目标／处理意图，效果弱于后续版本。不能再把旧版描述为“完全没有同步考虑”。它也不是整个分层改造之前的版本，备份中已经包含主计划与校正层。
5. 后续 M6S 修正将卷绕与旁工序机台搭配组合纳入候选批次，按业务经验保留高效组合。该改进由本人确认；本次备份不足以逐行还原后续完整实现。
6. PC 审核及人工调整计划时间从约 3 小时降到 20 分钟，是后续计划工作流程结果；不是求解时间，也不单独归因于某一处修改。
7. **稀疏候选批次与逐步扩展的迭代求解机制由本人设计。** 初始只使用稀疏候选批次，根据求解结果逐步增加候选并重新求解，以控制初始模型规模，再逐步丰富可选方案。

## 2. 先讲业务，再讲模型

用户是生产计划员（PC）。其核心任务是：在不同工厂、制造平台、MU、车间和设备能力之间分配需求，并形成能够协调卷绕与旁工序的生产安排。

**简短工序说明：** 本项目重点涉及卷绕及与之配套的旁工序。卷绕机台能生产哪些型号、以什么速度生产，以及旁工序能同时支撑多少卷绕机台，都会影响产量。M6S 没有明确固定拉线；多台卷绕机台生产同型号时可以共享旁工序设备，但一个连续批次内旁工序设备不能随意切换。因此，总产能够用仍可能排不出可执行的设备搭配与时间安排。这是本项目相关环节的简化说明，不是完整电池制造流程。

**两类不同问题：**

- **规模问题：** 需求、机台、型号、日期和跨工序选择组合过大，单个日计划难以承载宁德规模。
- **可用性问题：** 模型在汇总能力上合理，仍可能遗漏共享资源的连续占用，或低估实际换型对可用工时的影响。

前者推动主计划分配与下层拆分，后者推动排程后校正和后续 M6S 候选结构改进。两类问题有关联，不能把所有改造归结为“换一个求解器”。

## 3. 决策层次与颗粒度总表

| 阶段 | 决策或处理问题 | 主要颗粒度 | 输入与给定条件 | 输出及交接 |
|---|---|---|---|---|
| 运行范围 | 本次计算哪些业务范围 | 工厂、制造平台；日计划进一步按 MU | 配置、版本、计划起点与范围 | 模型任务及输入快照 |
| 净需求 | 已有供应覆盖后还需生产多少 | 型号、需求时间、相关包装／工艺属性及业务范围 | 原始需求、库存、WIP／实际达成、已有工单等 | 各期净需求与追溯关系 |
| 主计划 | 需求如何分配给 MU／车间和资源能力 | 聚合设备组 × 型号 × pack × 路径 × 时段／子时段 | 净需求、工艺、设备组能力、日历与产能余量 | 分范围产量，供下层计算份额及适用车间 |
| 层间转换 | 哪个下层任务承接多少需求、哪些资源选择 | 型号 × MU 份额；相关车间与机台候选 | 主计划产量结果 | 日计划需求分配与候选范围限制 |
| 日计划 | 哪台卷绕机做哪个型号、形成什么连续批次、怎样搭配旁工序 | 卷绕具体机台 × 型号 × 起止日；周期产量和旁工序机台配置 | 分配需求、可用机台、节拍、工单、维修、样品等 | 批次、顺序、周期产量、资源使用等 |
| 候选控制 | 先保留哪些批次，何时扩展 | 机台 × 型号 × 起止日候选 | 可用时间、业务筛选规则、求解中的欠交等 | 规模受控的候选集合；部分分支增补 |
| 后处理 | 将模型结果整理成具体排程数据 | 具体机台、型号、日期、借机／拉线安排等 | 日计划解、取整与业务整理规则 | 计划表、资源使用、KPI、校正层输入 |
| 排程后校正 | 在保留主要安排的基础上修正更细的约束影响 | 原批次关联、机台、型号、日期与产量偏差 | 前层排程结果、详细换型与日产能等 | 微调后产量／时间安排及偏差输出 |
| 业务使用 | 是否接受、还需怎样调整 | 计划记录、批次及异常 | 最终计划与业务判断 | PC 审核、人工调整；不等于主计划层人工审批 |

**时间粒度说明：** 主计划并非简单“所有时间都按月”。旧版代码包含近端按日、远端按月及子时段的组织方式；日计划在范围内保留日级安排。具体天数、月份与有效范围由运行配置决定。

**MU 说明：** 本文沿用系统字段 MU，视为计划拆分与需求承接的业务范围标识；其客户内部全称和组织定义未补充，不自行展开英文缩写，也不把 MU 与单个车间直接等同。

## 4. 输入怎样转为决策对象

| 输入类别 | 关键内容 | 用于判断什么 |
|---|---|---|
| 运行配置与任务标识 | 工厂、平台、MU、计划范围、运行类型、版本／分析 ID | 任务边界与可复现范围 |
| 产品与需求 | 型号、需求时间、需求数量及相关属性 | 需要满足谁、何时满足、缺多少 |
| 库存、在制、实际达成及工单 | 数量、状态、工艺位置、已有安排 | 净需求及必须衔接的已有生产 |
| 设备与设备组 | 工厂、车间、设备类型、具体机台、能力归属 | 主计划聚合能力与日计划具体机台 |
| 节拍与工艺路径 | 型号适配、速率、工序关系、提前期 | 哪些机台能做、数量如何转为工时及配套需求 |
| 日历与能力参数 | 可用时段、停开车间、维护、利用率等 | 每期真正可用的能力 |
| 业务限制与优先级 | 固定计划、样品、机台限制、目标配置等 | 哪些安排应保留，哪些候选可选及如何取舍 |
| 主计划产量 | 工厂、MU、车间、型号、pack、路径、月份、周期、数量等 | 下层需求份额与资源候选限制 |
| 日计划结果 | 批次／顺序、机台、日期、产量与资源配置 | 后处理与校正模型的基准 |

这些是当前读取流程涉及的类别，不表示每次运行全部输入都生效，也不表示所有字段都是自由决策变量。主读取链见 [read_data](D:/yhl_back/atl_aps_2021/src/data_parser.py:154)。

## 5. 决策卡一：先解决输入可复现与团队接口

**问题：** 算法输出有异常时，能否重新取得当时完全相同的输入，区分数据变化与算法问题？

**[业务已确认]** ATL IT 负责人倾向算法直接读取数据库，并不希望其团队承担文本输入构建。我通过几次真实优化问题的排查分享，解释固定输入对复现和诊断的重要性。最终采用版本化文本输入，由 ATL 维护，每次运行有输入编号，系统版本管理已经落地。我方负责算法，ATL IT 负责前后端。

**颗粒度：** 一次运行及其完整输入集合，不只是某张表的单个字段。

**[代码已确认]** 备份支持 CSV、SQL 与 Excel 等读取方式，包含 `csv_input` 快照备份逻辑；服务器请求字段有版本及分析 ID。这些是支持机制，不能单靠它们还原完整系统版本管理。

**取舍：** 文本文件增加生成与维护工作，但提供固定的诊断边界。数据库快照同样可以满足可复现要求，不能说数据库天然无法复现。

**PM 表达重点：** 将争论从“喜欢文件还是数据库”转成非功能需求、实际排障证据与责任分工。

证据：[CSV 读取](D:/yhl_back/atl_aps_2021/src/run_model.py:311)、[输入来源选择](D:/yhl_back/atl_aps_2021/src/run_model.py:332)、[输入快照](D:/yhl_back/atl_aps_2021/src/data_struct.py:870)、[请求参数](D:/yhl_back/atl_aps_2021/server/server.py:165)。

## 6. 决策卡二：明确计算边界，并先算净需求

**问题：** 不能将全部客户需求直接当作新增生产量，也不能在不同范围重复承接相同需求。

**[代码已确认]** 主计划和日计划分别按配置组织范围；日计划任务含工厂、制造平台和 MU。净需求更新先处理库存、在制／实际记录，再处理需求和已有工单等，日计划还使用主计划形成的 MU 需求份额。

**颗粒度：** 从原始型号需求，转为带时间、已有覆盖和任务归属的净需求。这里的净需求不等于一个脱离日期的“总需求减总库存”。

**决策含义：** 先确定真正还需要新增生产的数量，才能比较分配方案；已有工单和固定安排会限制后续重新优化的自由度。

**输入 → 输出：** 原始需求＋已有供应与安排 → 分范围、分时间的净需求及相关追溯记录。

**仍需核实：** 各类库存／WIP 的现场更新频率和所有例外口径；当前未读取生产样本进行数量对账，不声称所有物料数据已验证无误。

证据：[主计划范围](D:/yhl_back/atl_aps_2021/src/run_model.py:365)、[日计划范围](D:/yhl_back/atl_aps_2021/src/run_model.py:396)、[净需求更新](D:/yhl_back/atl_aps_2021/src/data_parser.py:2786)、[在制及实际记录处理](D:/yhl_back/atl_aps_2021/src/data_parser.py:2926)。

## 7. 决策卡三：为宁德规模增加主计划

**[业务已确认]** 原来只有日计划。从东莞向宁德推广时，宁德工厂规模过大，因此由本人增加主计划，先完成需求与能力分配，再运行下层日计划。

**为什么不是原模型直接放大：** 型号、资源、日期和连续批次选择叠加，组合规模增长；如果每个局部日计划独立争取全部需求，又缺少跨范围协调。主计划提供统一的分配依据。

**[代码已确认]** 主计划按工厂、设备类型及子类等组织聚合设备组；日计划的卷绕设备组进一步纳入具体机台。主计划仍保留型号、pack、路径、时段等相关决策，并非只有总量表。

**颗粒度取舍：** 上层保留影响需求承接和主要产能分配的信息，下层再确定具体机台和连续批次。主计划不是详细机台排程，也不要直接套用松下“MRP 先选替代料路径”的故事。

**输出：** 分工厂／MU／车间等范围的型号产量结果，供下层分配与资源筛选。

**产品判断：** 规模扩展需要调整决策分工；不只是把同一模型部署到更多工厂。尚未补充与哪些业务方共同确定此架构，不自行添加审批人或正式评审流程。

证据：[设备组构造](D:/yhl_back/atl_aps_2021/src/data_parser.py:2406)、[时间粒度](D:/yhl_back/atl_aps_2021/src/data_parser.py:310)、[生产量变量](D:/yhl_back/atl_aps_2021/src/main_plan_model.py:3607)。

## 8. 决策卡四：主计划保留产能余量，换取下层可承接

**[业务已确认]** 主计划中对产能做一定折扣，避免上层分配过满，下层加入具体批次及设备要求后无法完成。上线半年，未出现因主计划分配错误导致的日计划欠交；这种安排会增加额外转型。

**颗粒度：** 在上层能力预算中保留余量，而非为每张订单独立预留相同百分比；现场具体折扣落在哪类能力参数、如何设置尚未确认。

**设计解释：** 上层粗化会丢失部分详细资源冲突。保留能力余量可以降低分配过紧的风险，但可能让需求分布更分散，使下层增加转型。这是可承接性与效率的取舍，不是无代价的分层。

**代码边界：** 当前代码可见利用率和开工比例等能力调整机制，但没有足够证据将其中某一字段唯一认定为本人描述的现场折扣配置，因此不写具体系数或公式。

**结果口径：** “没有因主计划分配错误造成日计划欠交”限定了观察期和原因，不能扩大为“所有订单零欠交”“数学上保证所有下层可行”或“实际交付率 100%”。

**建议方法：** 如再次设计，会同时看下层欠交、能力余量、额外转型及端到端时间，并按平台与需求组合比较折扣效果。这是建议，不声称当时已建立完整动态调参闭环。

相关机制：[利用率读取](D:/yhl_back/atl_aps_2021/src/data_parser.py:2246)、[能力约束](D:/yhl_back/atl_aps_2021/src/main_plan_model.py:5668)。

## 9. 决策卡五：主计划怎样成为下层输入

**[业务已确认]** PC 不先审核主计划。主计划完成后直接分布式运行日计划；最终计划的 PC 审核与调整属于后续工作流程。

**[代码已确认]** 日计划读取 `master_output/produced.csv` 或对应结果表。可见字段包含 `factory_name, mu, plant, machine_device_type, product_name, pack, path, month, period, sub_period, product_quantity`。

代码主要形成两种交接：

1. **需求数量归属：** 从主计划产量汇总出“型号 × MU”的份额，再用于日计划净需求分配。旧版函数先按多个字段汇总，计算份额时进一步按型号及 MU 汇总；不能声称所有原始月度产量记录均原样锁死到下层每一天。
2. **资源候选范围：** 根据主计划选中的车间等信息限制下层部分卷绕机台候选，同时保留样品、固定计划、工单及借机等例外。

**重要区别：** 该备份不能支持“主计划将所有工艺路径一律锁死”的说法：路径过滤函数中，从主计划读取可用路径的调用被注释，实际初始化为空集合映射。不要借用松下 MRP 的路径收敛逻辑来补齐 ATL。

**部署边界：** 备份的 `run_model` 内部顺序遍历任务块。现场分布式调度由本人确认，外层服务如何派发、是否采用何种队列及机器数量未核实，不编造实现。

证据：[读取主计划结果](D:/yhl_back/atl_aps_2021/src/data_parser.py:3203)、[份额计算](D:/yhl_back/atl_aps_2021/src/data_parser.py:3322)、[候选机台筛选](D:/yhl_back/atl_aps_2021/src/data_parser.py:5460)、[路径过滤边界](D:/yhl_back/atl_aps_2021/src/data_parser.py:6295)、[单入口循环](D:/yhl_back/atl_aps_2021/src/run_model.py:663)。

## 10. 决策卡六：日计划围绕连续批次与机台搭配求解

**[业务已确认]** 日计划主要专注于生产批次和机台搭配，其他更细的换型影响由校正模型微调。

**[代码已确认]** 连续批次候选的关键索引为：`(machine_group, product, start_day, end_day)`，用二元变量选择是否启用。对卷绕而言，日计划的设备组已经包含具体机台。生产量变量再表达各期数量，并与设备配置、工序关系、连续生产等约束关联。

**两种不同决策：**

- **开哪一个批次：** 哪台机、哪个型号、哪段连续时间。
- **批次怎样使用资源：** 每期生产多少、需要多少配套机台、跨工序能力如何匹配。

**设计解释：** 将“连续生产一段时间”作为候选对象，可以直接表达批次完整性；代价是起止时间与机台组合很多，需要控制候选数量。它不是简单按天分摊数量。

**旧版与后续版的区别：** 当前可见的单机连续区间候选，不应直接解释成已经包含后来全部卷绕—旁工序组合的候选批次；后续版本改变了候选表达的业务内容。

证据：[连续批次构造](D:/yhl_back/atl_aps_2021/src/main_plan_model.py:11378)、[生产量变量](D:/yhl_back/atl_aps_2021/src/main_plan_model.py:3607)、[工序数量关系](D:/yhl_back/atl_aps_2021/src/main_plan_model.py:5188)、[配套机台关系](D:/yhl_back/atl_aps_2021/src/main_plan_model.py:5401)。

## 11. 决策卡七：候选先筛选，部分分支按需要扩展

**问题：** 如果每个型号、机台和所有起止日组合都一次性加入模型，规模会很大。

**[业务已确认] 本人设计：** 初始仅使用稀疏候选批次，先求解一个候选规模受控的模型，再根据求解结果逐步增加候选批次并重新求解，形成迭代机制。

**[代码已确认]** 存在连续批次的稀疏筛选函数；近端保留及远端起点／长度步长用于控制候选。部分求解流程先限制可用机台，再根据欠交等结果给当前或新增机台补充批次候选。

**颗粒度：** 增减的是“某机台做某型号、从哪天到哪天”的候选，以及相应的可用机台范围。

**取舍：** 候选少，求解更容易；候选过少，可能错失更好安排。扩展机制缓解这一问题，但依赖分支、规则和终止条件，不能声称每次日计划都执行相同扩展步骤。

**目标口径：** 某些阶段将欠交、机台使用、连续批次数量、借机及其波动等放在组合目标中。不能把所有运行概括成严格的“先零欠交，再最少换型”字典序保证。

**面试术语：** 可以说 iterative solving with a sparse initial candidate set and progressive candidate expansion。该机制由本人设计，面试应明确使用 I designed；这不等于每段相关函数均由本人原创。代码有增补变量不等于已实现带对偶定价的严格列生成，也不提供全局最优保证。

证据：[稀疏筛选](D:/yhl_back/atl_aps_2021/src/main_plan_model.py:11368)、[候选变量增补](D:/yhl_back/atl_aps_2021/src/main_plan_model.py:11119)、[限制机台与扩展流程](D:/yhl_back/atl_aps_2021/src/main_plan_model.py:14967)、[组合目标](D:/yhl_back/atl_aps_2021/src/main_plan_model.py:15124)。

## 12. 决策卡八：M6S 从同步目标走向组合批次

**[业务已确认]** M6S 不存在明确固定拉线。同型号的多台卷绕机台可以共享旁工序设备，旁工序设备在一个连续批次中不能切换。旧版本已有尽可能同开同收的目标，但效果不及后续版本。

**真正遗漏的内容：** 总能力和同步偏好，没有充分表达哪些设备应作为一组，在一个连续批次内共同占用资源。因此，即使目标倾向同步，也可能输出难以实际执行的组合。

**后续决策：** 将卷绕机台与旁工序机台的搭配组合纳入候选批次，并依据业务经验优先保留高效组合，控制新增组合带来的复杂度。

**颗粒度变化：** 从单机批次及汇总／配套关系，进一步表达一组协同资源的批次安排。这里描述本人确认的业务建模变化，后续版本的完整变量索引、同步是否逐项作为硬约束及约束公式未核实。

**为什么只加同步权重可能不够：** 软目标只是让某种安排更受偏好，不能单独排除共享设备被不合适地分配或在连续占用中发生冲突。关键是资源组合与时间占用的表达是否足够。

**示意例子，仅用于讲解：** 卷绕 A、B 做同型号，可以共享旁工序 X。如果只核对一天总能力，不追踪 X 在整个连续批次中的占用，另一个批次仍可能在不适当的时间被分配到 X。候选中明确 A/B 与 X 的搭配，再约束连续占用，有助于排除这种安排。A、B、X 是说明符号，不是现场资产编号或实际数值。

**验证与结果：** 修正后由 PC 审核。后续 PC 审核及人工调整时间从约 3 小时降到 20 分钟；没有补充逐批实际生产验证或单项修正的独立收益评估。

**代码边界：** 备份存在配套机台数量与批次关系，以及固定拉线相关的同步约束；它们支持分析旧版能力，不能当作后续 M6S 组合批次的完整代码证据。本人说明旧版已有 M6S 同步目标，不因未定位其唯一对应函数就将该业务事实否定。

参考：[配套机台与批次关系](D:/yhl_back/atl_aps_2021/src/main_plan_model.py:10230)、[固定拉线连续区间关系](D:/yhl_back/atl_aps_2021/src/main_plan_model.py:10643)。后者不能直接等同于 M6S 后续实现。

## 13. 决策卡九：把日计划解整理成具体排程

**[代码已确认]** 日计划输出流程不仅写文件，还包含周期处理、产量取整、拉线／借机数量协调及换型信息处理，然后输出计划、资源使用和 KPI 等。

**颗粒度：** 从内部模型变量，整理到机台、型号、日期与数量等业务记录。卷绕输出还会对包装、路径和子时段等维度汇总。

**设计解释：** 汇总、取整和具体资源展开可能改变原始模型数量之间的匹配，因此后处理之后仍需检验更细的可行性，不能把 solver 返回 feasible 当成最终计划天然可执行。

**输出 → 下一层：** 日计划 `result.xlsx` 等结果被保留，作为排程后校正读取的前层结果；原始输出另有备份。不是人工重新录入一个不相关计划。

证据：[日计划输出主流程](D:/yhl_back/atl_aps_2021/src/output.py:4620)、[卷绕日计划表](D:/yhl_back/atl_aps_2021/src/output.py:3656)、[结果交接与备份](D:/yhl_back/atl_aps_2021/src/data_struct.py:893)。

## 14. 决策卡十：增加排程后校正，分担细节复杂度

**[业务已确认]** 由本人增加校正层，目的是避免上层规划承载过多细节，让日计划聚焦生产批次与机台搭配，换型等细节由校正模型微调。

**[代码已确认]** 日计划的一部分能力约束使用平均换型时间，并非完全不考虑换型。校正模型重新构建更细的跨日换型、日产能及机台关系等，结合前层安排重新优化。

**颗粒度：** 以已有批次与顺序为基准，细化机台、型号、日期及产量安排；保留主要顺序关系，并允许必要调整。不能说所有数量、时间都原封不动，也不能说完全自由地重新排一次全厂。

**目标：** 尽量减少相对前层的批次产量、机台型号总量和顺序等偏差；输出偏差记录。当前函数名含 `after_gantt`，但它是优化校正，不只是甘特图展示或格式转换。

**取舍：** 减轻前层求解负担，同时引入需要修正的偏差。因此应该检查校正后是否仍满足需求、偏差集中在哪里，而不是只看前层结果。

**可见输出：** `after_gantt_slack.csv` 按机台／型号／起止区间记录偏差，`after_gantt_ttl_slack.csv` 按机台／型号记录总量偏差。偏差值需结合变量定义解释，不直接等同报废或实际欠交。

**保证边界：** 校正模型仍可能产生偏差或例外；有校正层不等于已证明任何输入都能得到零违背、实际可执行的计划。

证据：[日计划平均换型与能力处理](D:/yhl_back/atl_aps_2021/src/main_plan_model.py:18139)、[校正模型](D:/yhl_back/atl_aps_2021/src/main_plan_model.py:18422)、[前层顺序关系](D:/yhl_back/atl_aps_2021/src/main_plan_model.py:11685)、[偏差输出](D:/yhl_back/atl_aps_2021/src/main_plan_model.py:18504)。

## 15. 把整个流程连成一次运行

下面是逻辑示意，不是可以直接执行的原始代码：

```text
保留运行输入与版本，确定工厂／平台及计划范围
读取需求、库存、WIP、实际达成、工单、工艺与资源数据
计算净需求

主计划：在保留一定产能余量的条件下分配需求与主要能力
    输出分范围产量
    转换为 MU 需求份额与下层资源候选限制

现场部署：直接分布式运行各范围日计划，不先由 PC 审核主计划
    构造连续批次与机台配置
    筛选候选；部分分支按欠交等结果扩展
    求解并整理具体排程、取整、资源及换型信息
    排程后校正：按更细约束微调前层安排并输出偏差

PC 审核最终计划并作必要人工调整
```

后续 M6S 的组合批次改进发生在日计划候选与资源表达部分，不能写成当前旧备份已经实现全部后续规则。主计划读写与下层调用可见于 [入口](D:/yhl_back/atl_aps_2021/run.py:27) 及 [运行器](D:/yhl_back/atl_aps_2021/src/run_model.py:663)。

## 16. 面试主陈述：约 2–3 分钟，中英对照

> At ATL, I worked on a production planning system. When the solution expanded from Dongguan to the much larger Ningde factory, the existing daily planning model needed a different structure to handle the scale.

在 ATL，我参与生产计划系统。方案从东莞推广到规模大得多的宁德工厂时，原有日计划模型需要改变结构，才能承载更大规模。

> I added a master planning layer to allocate demand across planning areas and workshops before detailed scheduling. After it finished, the system ran daily planning jobs in a distributed setup, without a separate planner review of the master plan.

我增加主计划层，在详细排程前先把需求分配到不同计划范围及车间。主计划完成后，系统直接分布式运行日计划，不额外经过计划员对主计划的审核。

> I used a capacity discount in master planning to leave room for detailed constraints. During the first six months after deployment, we did not see daily-plan shortfalls caused by incorrect master allocations. The trade-off was additional changeovers, so this was not a cost-free simplification.

我在主计划中使用产能折扣，为详细约束留出余量。上线后的半年中，没有出现因主计划分配错误造成的日计划欠交；代价是增加额外转型，因此这种简化也有成本。

> Daily planning focused on continuous production batches and machine assignments. I also added a post-scheduling correction model. It handled finer changeover and capacity effects while keeping the main schedule structure, so we did not have to solve every detail together in the daily model.

日计划重点求解连续生产批次和机台搭配。我还增加了排程后校正模型，在保留主要排程结构的基础上处理更细的换型和产能影响，避免日计划一次性求解所有细节。

> I designed an iterative solution approach that started with a sparse set of candidate batches, then used the solve results to add candidates progressively and re-solve. This controlled the initial model size while expanding the available choices over successive iterations.

我设计了迭代求解机制：初始仅使用稀疏候选批次，再根据求解结果逐步增加候选并重新求解。这让初始模型规模可控，同时在后续迭代中逐步丰富可选方案。

> A separate challenge was M6S, where winding machines shared supporting equipment without fixed lines. The earlier version already encouraged synchronized starts and finishes, but that was not enough to capture the resource combinations needed during a continuous batch. I later included compatible winding and supporting-machine combinations in the candidate batches, retaining efficient options based on business knowledge.

另一个难点是 M6S：卷绕机台在没有固定拉线的情况下共享旁工序设备。旧版已经鼓励同开同收，但仍不足以表达连续批次所需的资源组合。后续我将可行的卷绕与旁工序机台搭配纳入候选批次，并依据业务经验保留高效组合。

> The revised plans were reviewed by the planning team. Their review and manual adjustment time later fell from about three hours to twenty minutes. That measured planner effort, rather than solver runtime, and I would not attribute the entire improvement to one change.

修正后的计划由 PC 审核。后续审核及人工调整时间从约 3 小时降到 20 分钟。这衡量的是计划员投入，不是求解时间，我也不会把全部改善都归因于某一项修改。

> The product lesson was to decide which level should own each decision, make the handoffs explicit, and check whether the final output reduced the planner’s work.

产品上的体会是：明确每一层负责什么决定、清楚定义层间交接，并检查最终输出是否减少了计划员的工作。

## 17. 关键追问：可直接口述的回答

### Q1. What did you personally contribute?

> The original solution had daily planning. I added master planning when the move to Ningde created a scale problem, and I added the post-scheduling correction layer to separate detailed adjustments from batch and machine decisions. I also designed the iterative mechanism that started with sparse candidate batches and progressively added candidates based on solve results. Other contributions included the M6S resource-combination improvement and agreeing on reproducible inputs with ATL’s IT team. Our team owned the algorithms; ATL owned the application front end and back end.

原方案只有日计划。我为宁德推广带来的规模问题增加主计划，并增加排程后校正层，将细节调整与批次、机台决策分开。我还设计了初始使用稀疏候选批次、根据求解结果逐步增加候选的迭代机制。其他贡献包括 M6S 资源组合改进，以及与 ATL IT 明确可复现输入的方案。我方负责算法，ATL 负责应用前后端。

### Q2. Why did you add master planning?

> Ningde was much larger than Dongguan. I separated the broad demand allocation from detailed machine scheduling. That gave the daily jobs a defined scope and reduced the combinations each job had to consider. The important trade-off was preserving enough capacity information in the master plan for the allocations to remain workable.

宁德规模比东莞大很多。我将较大范围的需求分配与具体机台排程分开，让日计划有明确范围，减少每个任务需要考虑的组合。关键取舍是：主计划仍需保留足够的产能信息，使分配能被下层承接。

### Q3. How did you prevent bad allocations from the master plan?

> I used a capacity discount to leave room for details that the master plan did not represent fully. We did not observe daily-plan shortfalls caused by incorrect master allocations during the first six months after deployment. However, it could add changeovers. I would describe that as an observed trade-off, not a mathematical guarantee of feasibility.

我用产能折扣为主计划未完整表达的细节留余量。上线半年没有观察到因主计划分配错误导致的日计划欠交，但会增加转型。这是有观察依据的取舍，不是数学上的可行性保证。

不能补写折扣具体百分比或自动学习调参机制。对方问“怎样定折扣”时，应提供真实历史方法；尚未回忆清楚可以坦诚说明，不编造实验结果。

### Q4. Did planners review the master plan before daily scheduling?

> No. The master output fed directly into the distributed daily planning jobs. The planner review I mentioned was for the resulting schedules and any manual adjustments, not an approval step between master and daily planning.

没有。主计划输出直接进入分布式日计划。我提到的 PC 审核，是对后续排程结果及人工调整的审核，不是主计划到日计划之间的审批步骤。

### Q5. Why did you need a correction model?

> Daily planning focused on the batch structure and machine assignments, with some changeover effects approximated. The correction model used the existing schedule as a starting point and handled finer changeover and capacity constraints. That kept the main problem manageable, but we still had to check the final quantities and any deviations.

日计划聚焦批次结构和机台搭配，部分换型影响采用近似处理。校正模型以已有排程为基础，处理更细的换型及产能约束，让主要问题规模可控，同时仍需检查最终数量和偏差。

### Q6. What exactly was missing in the earlier M6S model?

> The earlier version already encouraged the winding machines to start and finish together. The gap was that synchronization alone did not fully represent which winding and supporting machines had to work as a group during a continuous batch. I improved the candidate batches to include those compatible resource combinations.

旧版已经鼓励卷绕机台同开同收。缺口在于，同步本身不足以完整表达一个连续批次中哪些卷绕和旁工序设备必须作为一组协同。我改进候选批次，将这些可行资源组合纳入其中。

### Q7. How did you balance model size and solution quality?

> I addressed model size at several levels. Master allocation reduced the scope of each daily job. I designed an iterative mechanism that started with sparse candidate batches, then added candidates and re-solved based on the solve results. The correction layer addressed finer scheduling effects. Each simplification could lose some flexibility, so final feasibility and planner effort mattered alongside runtime.

我从多个层次控制模型规模：主计划缩小各日计划范围；我设计了初始使用稀疏候选批次、再根据求解结果增加候选并重新求解的迭代机制；校正层处理更细的排程影响。每种简化都可能损失灵活性，所以除了运行时间，还要看最终可行性和计划员投入。

### Q8. How did you validate the improvement?

> The planning team reviewed the revised schedules. Their review and manual adjustment time later decreased from about three hours to twenty minutes. Separately, over six months we saw no daily-plan shortfalls attributable to incorrect master allocations. Those are different observations; neither means that every schedule was validated through actual production.

PC 审核了修正后的计划，后续审核及人工调整时间从约 3 小时降到 20 分钟。另外，半年内未观察到因主计划分配错误导致的日计划欠交。这是两类不同观察，都不能推出每份计划均经过实际生产验证。

### Q9. What would you do differently?

> I would validate representative shared-equipment scenarios earlier, including continuous batches and cases without fixed lines. I would also compare the final schedules across capacity-discount settings, looking at shortfalls, extra changeovers, and planner adjustments. That would help make the cost of the decomposition more visible.

我会更早验证共享设备的代表性场景，包括连续批次和没有固定拉线的情况。我也会比较不同产能折扣下的最终计划，同时看欠交、额外转型及人工调整，让分层的代价更清楚。这是建议，不声称当时已经全部实施。

## 18. 指标与最后复习清单

| 内容 | 可以说 | 不能扩大为 |
|---|---|---|
| 本人贡献 | 增加主计划与校正层，设计稀疏候选逐步扩展的迭代求解机制，改进 M6S 候选资源组合，推进输入版本方案 | 所有旧版日计划代码均为本人原创，前后端均由本人开发 |
| 分布式日计划 | 本人确认的现场部署方式 | 旧版循环本身就是并行实现，或擅自指定部署框架 |
| 产能折扣 | 留出余量，半年未见分配错误导致的下层欠交，代价含额外转型 | 所有需求零欠交、没有任何效率损失、全局可行性证明 |
| M6S 版本 | 旧版有同步目标，后续用资源组合批次改善 | 旧版毫无同步考虑，或备份已完整包含后续改进 |
| 3 小时 → 20 分钟 | PC 审核及人工调整时间 | 求解时间、全部 PC 工时，或单一修改的独立收益 |
| 90% | 计划部门拟减少 PC 人员的目标，执行未确认 | 已实现的人员或工作量下降 |
| 校正层 | 保留主要安排，处理更细约束并跟踪偏差 | 只是绘图，或必然消除所有业务不可行性 |

优先练熟：**宁德规模为何触发分层 → 各层决定什么 → 产能折扣的作用与代价 → 本人设计的稀疏候选与逐步扩展机制 → 日计划到校正层的分工 → M6S 为何同步目标不够 → 输入版本与 IT 协作 → PC 时间指标。**

仍可进一步补充但不影响使用本稿：产能折扣的具体制定与校准方法；参与架构确认的业务方；MU 的客户内部定义；后续 M6S 版本的完整候选索引与约束；额外转型的量级及应对措施。当前均保留事实边界，不自行补全。
