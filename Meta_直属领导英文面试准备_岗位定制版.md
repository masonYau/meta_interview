# Meta Manufacturing Operations Engineer：直属领导英文面试准备

更新：2026-10-29。基于本人简历、Meta Initial IC 指南、本次提供的完整 JD，以及本人补充的 ATL/松下事实。本稿取代此前通用初稿中的岗位定位和待填案例。以下英文是建议口述稿，问题为推演练习题，并非官方题库。

## 1. 收到 JD 后的关键判断

这是偏 CM 现场制造运营与持续工程的岗位。JD 明确要求产线建立和爬坡、每日产出和人力跟踪、布局与节拍优化、OEE、测试和复测、良率、工程变更执行及异常处理。不能把它理解成主要开发 MPS/APS 的岗位。

你的有力证据是：长期客户驻场、与 PC 紧密合作、生产约束理解、生产任务安排、资源协调、换型成本改善、Python/AI 数据处理、复杂问题排查，以及与客户 IT 的跨团队合作。本人确认松下/ATL 均为长期驻场，但只短时间参观车间，大部分生产知识来自计划员；所问现场工作中亲自做过生产任务安排，没有直接 CT 测量、设备/测试异常分析、良率分析或 MES 数据提取经历。这与三年以上高产量电子装配/测试现场经验有差距，不能仅靠术语学习或表达消除。

本次英文面试官是直属领导。准备目标是让对方判断：你的能力能覆盖岗位中的哪些具体问题；对其他现场职责，你是否有足够的相关经历与明确的学习方法。无需在开场罗列所有不足；被问到直接经验时要具体回答。

### 推荐的个人定位

我有制造计划与优化经验，能识别跨设备、跨工序的真实限制，排查造成计划不可执行的根因，并与业务和 IT 合作改进方案。我希望将这套能力用于更直接的制造运营工作。

> My strength is understanding how production constraints interact, finding why a plan does not work in practice, and working with other teams to improve it. My background is in manufacturing planning and optimization, and I want to apply that experience more directly to manufacturing operations.

不要将“我是算法专家”作为整场主线。介绍算法时，要紧接着解释它改变了什么生产决定、解决了什么执行问题。

## 2. JD 与个人证据对应

| JD 任务 | 个人证据 | 面试中的准确定位 |
|---|---|---|
| 产能规划、瓶颈、人力效率 | 松下/ATL 设备与旁工序资源计划；汇丰人员配置 | 有直接规划分析经验；工厂人员管理、现场排班和实际减员需另证 |
| CT、换型、布局、物料流 | 松下模具/物料/工序协同及换型费用；ATL 共享设备限制 | 有相关过程与资源分析；不能自动声称测过 CT 或做过 SMT/FATP 布局审核 |
| 异常排查与持续改善 | ATL M6S 计划不可执行的返工 | 主案例，展示问题定义、根因、修正及复盘；不是良率失效分析的直接替代 |
| CM 与内部团队合作 | ATL IT 输入格式与职责争议 | 证明无直属管理权情况下的协作；不等于已有 CM 质量/交付问责经验 |
| 数据自动化、Python/AI | 汇丰 Dify 工作流与 benchmark | 证明相关数据能力；未做过良率看板就不能称已经交付过 |
| FPY/LPY、测试、OEE、ECO/PRQ、设备交叉认证 | 当前未有明确直接实例 | 掌握分析逻辑，坦诚说明直接经验范围，向面试官确认职责深度 |

## 3. 优先练熟的四个故事

1. **松下：业务结果。** 交付承诺与资源约束、减少换型、客户测算费用。
2. **ATL M6S：返工与根因排查。** 总产能可行不等于共享设备在时间上可执行。
3. **ATL IT：跨团队分歧。** 以实际排障过程说明输入复现需求，达成输入版本管理方案。
4. **汇丰：数据与 AI。** 从非结构化记录提取特征并校验输出；为数据自动化能力作补充。

ATL 规模化和通用框架保留作技术追问。除非面试官主动问优化深度，否则中石油数学方法不占主要时间。

## 4. 自我介绍：约 75–90 秒

> Hi, I’m Jinfeng. My background is in operations research, mainly manufacturing planning and resource allocation.
>
> I currently work at HSBC on capacity planning and data workflows. Before that, I spent more than four years at Youhualin, where I led a small algorithm team and worked with manufacturing customers, including Panasonic Electronic Materials and ATL.
>
> At Panasonic, I worked with the production planning team on delivery priorities, material constraints, equipment capacity, and mold availability. The project helped reduce mold changes and the related cleaning costs.
>
> At ATL, I worked on battery production scheduling. I corrected a model that missed how shared equipment had to be coordinated over time. The revised plan was reviewed by the production planning team. The time they needed to review and manually adjust the plan went from about three hours to twenty minutes.
>
> My strength is combining data analysis with a clear understanding of production constraints and working across teams to solve practical problems. I’m interested in bringing that experience closer to day-to-day manufacturing operations.

中文记忆：背景 → 两段制造经历 → 松下结果 → ATL 实际限制及 PC 审核及人工调整效率 → 数据、生产理解、合作 → 动机。可以明确长期客户驻场；不要把它等同于长期在产线操作、观察或直接负责工艺与测试。3 小时到 20 分钟指 PC 审核及人工调整计划的时间，不称算法运行时间或整个排程流程时间。

## 5. 主案例一：松下，业务结果与取舍

### Q: Tell me about a manufacturing improvement project.

> One example is a planning and scheduling project for Panasonic Electronic Materials, producing copper-clad laminates.
>
> The challenge was that delivery priorities, materials, equipment, and molds were closely connected. We had to protect delivery commitments while reducing unnecessary mold changes.
>
> I was the algorithm lead. I worked with the production planning team to understand the requirements and led the planning solution design.
>
> We separated monthly material analysis, daily resource planning, and short-term scheduling. For mold-calendar decisions, we combined optimization with local adjustments, checking available mold sets and the effect on existing orders before re-solving the plan.
>
> After deployment, mold changes decreased by around ten per month. Panasonic estimated the cleaning cost at RMB 30,000 per change, so the estimated monthly savings were about RMB 300,000.
>
> Over a three-month period, the planning results showed 99.9% fulfillment against confirmed delivery dates. This was a planning metric, rather than an actual shipment metric.
>
> The key lesson was to connect the technical solution to delivery priorities, production constraints, and measurable business outcomes.

中文要点：生产问题 → 我的角色 → 三层与模具安排 → 客户测算费用 → 计划指标边界。不要把 99.9% 称为良率、实际出货准时率或改善了 99.9%。

### 追问 1：How did you calculate the savings?

> The estimate came from Panasonic. Each mold change involved cleaning, which they estimated at RMB 30,000. With around ten fewer changes per month, the estimated cleaning-cost reduction was about RMB 300,000 per month. This refers specifically to cleaning costs.

不要额外加入设备停机、人工、良率收益；本人没有给出这些测算。

### 追问 2：What does the 99.9% mean?

> It was a confirmed-date fulfillment metric in the planning results over three months. It was not a measurement of actual shipments. I would keep that distinction clear when discussing the result.

仍需核实按订单数还是数量统计，以及缺料订单如何计入。未核实前不自行指定分子分母。

### 追问 3：What was your personal contribution?

> I led the algorithm solution design and worked with the production planning team on requirements. I also guided other algorithm engineers. The complete system and its business results were team outcomes.

后续必须补本人亲自实现的模块、其他工程师职责以及验收分工；目前不要从“算法负责人”扩展为“整个项目所有交付均由我主导”。

## 6. 主案例二：ATL M6S，失败、返工和根因

### Q: Tell me about a time your solution did not work as expected.

> In the ATL M6S scheduling project, my initial model missed an important production constraint.
>
> The platform did not have clearly defined production lines, so I modeled winding machines individually and checked the total capacity of the supporting processes. I did not include the need to coordinate the start and finish times of machines producing the same model.
>
> The problem was that several winding machines could share supporting equipment. Once a continuous winding batch started, that equipment could not switch to another batch. The plan could therefore meet the total capacity limits and still be impossible to execute.
>
> I corrected the model by adding combinations of winding machines and supporting equipment to the candidate batches. To control model size, I used business experience to keep the more efficient combinations.
>
> The revised plan was reviewed by the production planning team. The time they needed to review and manually adjust the plan went from about three hours to twenty minutes. The lesson was that total capacity was not enough: I also needed to understand which resources were shared and how they were committed over time.

中文逻辑：遗漏真实限制 → 聚合产能掩盖时间冲突 → 组合批次表达共享资源 → 经验筛选控制规模 → PC 审核及人工调整时间改善 → 反思。本人确认由 PC 审核，审核及人工调整计划的时间从约 3 小时降到 20 分钟。该结果不是产线实测验证，不能扩展为所有计划实际生产均可执行，也不能归因于单个模型修正而排除其他项目改进。本人进一步确认该时间包括人工调整。

### 更短的 45–60 秒版

> At ATL, I once built a schedule that met total capacity limits but could not be executed. I had missed how winding machines shared supporting equipment during continuous production.
>
> The shared equipment could not switch freely between batches, so aggregate capacity checks were not enough. I changed the candidate batches to include compatible combinations of winding and supporting machines, and used business rules to keep the model manageable.
>
> The revised plan was reviewed by the planning team, and their time to review and manually adjust the plan went from about three hours to twenty minutes. I learned to check resource sharing and timing explicitly, instead of relying only on total capacity.

### 追问 1：What exactly was the root cause?

> The modeling error was treating supporting capacity as an aggregate resource. In reality, the equipment had to stay committed during a continuous batch, and multiple winding machines could share it. The model needed to represent those combinations and their timing.

### 追问 2：Why did you miss it?

> I relied too much on the absence of formal production lines and on aggregate capacity. I should have checked more carefully how machines worked together during an actual continuous batch. The missing constraint was in my model, so I needed to correct it.

不把原因全部推给业务“没提需求”。“没有明确拉线”解释建模背景，不免除自己的核实责任。

### 追问 3：Why not enumerate all machine combinations?

> That would create too many candidates. I used production experience to keep the efficient combinations and reduce the search space. The trade-off was that the candidate set was selective, so I would assess it by feasibility, coverage, and solution quality rather than claim that every possible combination had been explored.

### 追问 4：How did you validate the correction?

> The production planning team reviewed the revised plan. Their time to review and manually adjust the plan went from about three hours to twenty minutes. That is the validation and efficiency result I can describe. I would distinguish that review from verification through actual production execution.

### 追问 5：How would you prevent the same problem?

下列是从经历中推导的改进方法，除非本人确认已经执行，否则保留 would：

> I would review a representative batch from start to finish with the production team. I would check which equipment is shared, when it becomes committed, whether it can switch, and what has to start or finish together. I would also keep this example as a test case for future model changes.

与 JD 的连接：展示理解真实运行限制、技术排查及修正能力；不是声称做过电子装配失效分析或改善过 FPY。

## 7. 主案例三：ATL IT 分歧，跨团队影响力

### Q: Tell me about a disagreement with a cross-functional partner.

> In the ATL project, our team developed the optimization algorithm, while ATL’s IT team owned the front end and back end.
>
> Their IT lead preferred the algorithm to read directly from the database. He considered that a more production-ready approach and did not think his team should be responsible for preparing text input files.
>
> My concern was reproducibility. Optimization problems can take a long time to investigate. I wanted to preserve the exact input for each run so we could reproduce a problem without changes in the source data affecting the investigation.
>
> Rather than debating the file format alone, I walked him through several real model-debugging examples and showed why stable input mattered.
>
> We kept file-based input, and ATL maintained the input files. Version management was implemented in the system, with an input ID for each run so that we could identify the corresponding dataset.
>
> I learned that I needed to explain the operational reason behind the technical requirement and make the impact on the other team clear.

中文记忆：职责 → 对方诉求 → 我的复现需求 → 多次真实排障分享 → 同意文件输入和版本方案 → 体会。

本人补充确认：ATL 维护输入，系统版本管理已落地，因此可以说 implemented。文件生成的具体程序及负责人未进一步确认，不额外描述导出方式，也不加排障耗时下降数字。

### 追问 1：Was the database approach wrong?

> No. The database was a reasonable system data source. My requirement was to preserve the exact dataset used by a particular run. Those are separate concerns. The agreement in our project was to keep a versioned file as the algorithm input.

这是较稳妥的技术观点，避免陷入“文件一定比数据库更工程化”的立场。数据库也可通过快照、版本化数据等方法提供复现；如被问其他实现，可作为备选方案讨论，不声称本项目已实现。

### 追问 2：What did you do beyond explaining your own preference?

> I used real debugging examples to make the requirement concrete. I showed why we needed to reproduce the same model with the same input, and why changing data could make diagnosis harder. That helped us move from a preference about architecture to a specific requirement we could agree on.

### 追问 3：Did you just move work to their team?

> That was a fair concern, especially because they owned the application system. Our team owned the algorithm, while ATL owned the application and maintained the input files. The versioned input gave us a clear dataset to reproduce each run. I would still consider the maintenance cost when evaluating this design.

最终输入由 ATL 维护，版本管理已落地。直属领导仍可能追问：生成文件的过程、接口检查、维护成本及失败处理；这些具体机制尚未提供，不自行补写。

## 8. 与岗位直接相关的高优先级问答

### Q: Why are you suitable without direct FATP/SMT experience?

> My strongest direct experience is in manufacturing planning and optimization. I have worked on equipment constraints, material availability, changeovers, and coordination between production processes.
>
> For example, at ATL I corrected a scheduling problem caused by shared equipment, and at Panasonic I worked on planning decisions that reduced mold changes and cleaning costs.
>
> I would need to build deeper experience in electronics assembly, testing, and yield engineering. I would not present my planning work as direct ownership of those processes. The contribution I can bring is structured problem solving, data analysis, and experience working with manufacturing teams on practical constraints.

本人已确认具体经验边界。可以用下面一题解释长期驻场的内容，再回到共享资源、生产任务安排及 PC 审核及人工调整效率证据。不能承诺单靠快速学习就满足全部最低任职要求。

### Q: What hands-on factory experience do you have?

> I was based at the Panasonic and ATL customer sites for extended periods. Most of my work was with production planners, understanding production requirements and arranging production tasks. I made short visits to the workshops, but I did not spend extended time observing line operations.
>
> My direct experience is in production planning and arranging production tasks. I have not personally owned cycle-time measurement, equipment or test failure analysis, yield analysis, or MES data extraction.
>
> What I can bring is experience working closely with planners, understanding resource constraints, and correcting scheduling problems. I would need to develop more direct experience in the assembly and test processes covered by this role.

“驻场”说 customer-site experience；“车间”说 workshop / production floor。不要将 on-site 自动扩展成 shop-floor process ownership。本人已确认可以接受 JD 要求的频繁出差。

### Q: Are you comfortable with frequent travel?

> Yes, I’m comfortable with frequent travel across APAC and to other locations as needed. I spent extended periods at customer sites during the Panasonic and ATL projects, so I’m familiar with working away from my home office and collaborating closely with customer teams.

只说明可以出差与已有客户驻场经验，不推导过去已有 APAC 跨国出差经历或任何国家的工作许可。

### Q: Why do you want this role rather than another optimization role?

> What I enjoy most is understanding why an operation is not performing as expected and helping improve it. The algorithm is one tool I use.
>
> This role interests me because it connects daily production, technical problem solving, and data-driven improvement. I would like to take more responsibility for following an issue through to its operational result.
>
> I understand that this includes daily follow-up, coordination, and routine reporting as well as technical analysis. That is part of the ownership I would like to develop.

最后两段必须符合本人真实动机。不要把“更复杂的数学问题”作为加入现场岗位的主要理由。

### Q: Why leave HSBC?

> HSBC has given me valuable experience in capacity planning, data preparation, and aligning business rules across teams. I value that experience.
>
> My manufacturing projects helped me realize that I want to build my long-term career closer to production operations. I am particularly interested in how equipment, materials, and process decisions affect daily output.
>
> This opportunity would let me apply my analytical background while developing more direct ownership of manufacturing outcomes.

### Q: Tell me about your AI experience.

> At HSBC, I built Dify workflows to extract customer status and review-related information from unstructured case-manager notes. The structured information was validated before being used in optimization.
>
> I used historical text and generated edge cases for benchmark testing. The customer-status identification task achieved 98% accuracy on the project benchmark. That figure describes the benchmark task, not a guarantee of production-wide accuracy.
>
> The approach combined AI outputs with business rules, testing, and human review. For manufacturing, I would apply the same principle: use automation to speed up data preparation and investigation, while keeping important decisions tied to verified evidence.

准备样本规模、类别、测试集划分和具体错误类型。没有实际做过良率看板就用 “I would” 说明如何迁移，不称已有交付。

### Q: Did ATL reduce planning staff by 90%?

> ATL’s planning department intended to reduce the number of PC staff by around 90%, with the remaining staff focusing on data maintenance and plan adjustments. I cannot claim that the headcount reduction was actually implemented.

该数字不作为开场业绩。原简历“reduced planner workload by 90%”与本人当前说明不一致：后者是部门拟定的人力目标，既不是已实测工时下降，也不是已执行减员。如被追问，应主动澄清，避免继续沿用旧说法。

## 9. 现场情景题：明确是分析方法，不是既有履历

### Q: Output is below plan. What would you do?

> First, I would confirm the gap against the production and shipment plan, and identify the affected products and commitments.
>
> I would check that the data is comparable, then work with the factory owners to separate material shortages, downtime, cycle-time losses, staffing constraints, and quality losses.
>
> I would focus on the constraint that is limiting good output. With the relevant owners, I would agree on recovery actions, responsibilities, and escalation timing, then track whether output actually improves.

展开时注意：不能把低产出自动归因为排程差；先确认按小时、班次、产品和线别的数据及产品组合。

### Q: FPY drops, but final yield remains stable. How would you investigate?

> I would check whether rework or retesting is hiding a first-pass problem. I would confirm the metric definitions and compare first-attempt results with final results using unit-level records.
>
> Then I would break down the failures by station, tester, fixture, product, material lot, shift, and recent changes. I would work with process, test, and quality engineers to distinguish a real product or process issue from a measurement issue.
>
> Any immediate containment would follow the agreed quality process. After a suspected cause was identified, I would verify the corrective action with evidence and monitor for recurrence.

这是调查路径，不代表已查明根因。不要通过无限复测、放宽判定标准或删除失败记录“提高良率”。LPY 的完整名称、测试次数和统计窗口必须按团队定义确认，不自行解释为固定行业通用口径。

### Q: How would you improve OEE?

> I would first separate availability, performance, and quality losses, using consistent definitions and the relevant production period.
>
> Then I would look at which losses affect the line constraint most. Depending on the evidence, the priority might be downtime, slow cycles, changeovers, or quality losses.
>
> I would agree on a targeted action with the equipment, process, or test owner and measure the effect on good output as well as the OEE components.

不要承诺每台设备都满负荷，也不要把所有损失都归到同一类。设备 OEE 变好是否提高整线产出，需要看瓶颈和资源耦合。

### Q: How would you approach line balancing and labor efficiency?

> I would start with demand and available production time, then compare the required pace with actual station cycle times and work content.
>
> I would observe the process with the team and look for bottlenecks, waiting, rework, and material-handling delays. Any change in task allocation or layout would need to respect training, safety, quality, and equipment constraints.
>
> I would validate the change on a controlled scope and compare good output per labor hour, cycle time, and quality before extending it.

这是拟采用的方法，不把松下换模优化称为已经做过 FATP 人工线平衡。可用 ATL 共享设备经历解释：单工位优化可能影响其他工序，必须看整体。

### Q: How would you build an automated yield dashboard?

> I would first agree on the metric definitions, source systems, and the decisions the dashboard needs to support.
>
> I would preserve unit IDs, timestamps, station and tester IDs, first-attempt results, retests, and relevant material or process versions. I would check missing records, duplicates, and data freshness before calculating the metrics.
>
> The dashboard should let users move from a line-level issue to the affected station, failure category, and unit records. I would also define an owner and response process for important alerts.

与本人经历连接：Python、数据定义和 AI 校验能力相关；尚未证明已有 MES 良率项目。Tableau/JMP 熟练度按实际情况回答，不由 Python 经验自动推导。

### Q: How would you support an engineering change or line conversion?

> I would clarify the approved change scope, affected products and equipment, material and work-in-progress disposition, qualification requirements, and the implementation window.
>
> With the responsible engineering, quality, and operations owners, I would check readiness, the supply impact, acceptance criteria, traceability, and the rollback or escalation plan.
>
> After implementation, I would monitor the agreed production and quality indicators before considering the change stable.

目前是方法回答，不能称已独立签核 ECO、认证测试机或批准放行。PRQ、PMP、yield bridge 等内部术语的实际交付物和批准职责按团队定义了解。

### Q: How would you hold a CM partner accountable?

> I would make the target, data definition, owner, and due date explicit. For a missed target, I would separate the immediate recovery action from the investigation of the cause.
>
> I would review progress using agreed evidence and escalate early when a risk affects supply or quality. The goal would be a clear commitment and verified follow-through, rather than simply asking the partner to improve.

ATL IT 故事能证明解释需求和达成一致，但不能独立证明已经管理过 CM 的交付/质量绩效。这题可作为能力迁移回答。

## 10. 术语与计算：面试前至少能解释

以下为通用入门定义；实际口径以目标团队为准，不能把练习数字当作个人业绩。

| 术语 | 入门解释 | 容易误用的地方 |
|---|---|---|
| CT | 一个工序或工位完成一次处理的时间，需说明定义和单位 | 测试时间、上下料、等待是否纳入要明确 |
| Takt time | 可用生产时间 ÷ 需求量 | 它由需求推导，不等于实测 CT |
| FPY | 不经返工或复测，首次通过的数量占进入流程数量的比例 | 最终通过不等于首次通过 |
| LPY | JD 中与 FPY 并列的良率口径 | 完整名称、是否允许复测、窗口及分母需确认 |
| OEE | Availability × Performance × Quality | 时间基准、理想 CT、计数及损失分类必须一致 |
| Yield bridge | 为理解良率变化建立损失或贡献分解的工作表达 | 可能按工站/失效/版本拆分，实际格式和责任人需确认 |
| FACA | Failure Analysis and Corrective Action，失效分析与纠正措施 | 提出假设不等于验证根因，采取措施后需确认有效性 |
| MES | 制造执行系统，可能包含工序、设备、追溯与测试记录 | 对接范围按现场系统；没有实际经验就不说独立负责过 |
| FATP / SMT | 最终组装、测试与包装 / 表面贴装技术 | 了解概念不等于具有现场调试与质量处置经验 |

OEE 练习：计划生产 480 分钟、运行 420 分钟、理想 CT 30 秒、总产出 700 件、良品 665 件。A = 420/480 = 87.5%；P = 700×30/(420×60) ≈ 83.3%；Q = 665/700 = 95%；OEE ≈ 69.3%。这是假设同一时间范围、单一适用理想 CT 的入门例子，不混用停机和复测分母。

FPY 练习：1,000 件首次测试，900 件首次通过，后续复测又通过 80 件。在相同样本范围内，FPY 为 90%，最终通过率可为 98%；后者掩盖了额外测试负荷，需分别看待。不要将这个最终通过率未经确认直接命名为目标团队的 LPY。

参考：FPY 概念见 [ASQ Quality Glossary](https://asq.org/quality-resources/quality-glossary)；根因分析及其与改善措施的关系见 [ASQ Root Cause Analysis](https://asq.org/quality-resources/root-cause-analysis)。OEE 分量计算可对照设备数据产品的官方说明 [Leading2Lean Production Metrics](https://support.leading2lean.com/articles/8135196941-production-metrics-settings-definitions-calculations-and-acronyms)，现场停机归类仍应按实际配置核对。

## 11. 关键数字：当前采用的事实口径

| 数字 | 当前表述 |
|---|---|
| 松下每月约少 10 次换型 | 简历成果；本人确认由松下测算相关收益 |
| 每次 3 万元、约 30 万元/月 | 松下估算的换型清洗费用，保留 estimated，不扩展为总成本收益 |
| 确认交期满足 99.9% | 三个月的计划结果；不是实际出货率或良率 |
| ATL 90% | 计划部门拟减少约 90% PC 人员；没有确认已执行，不再写已减少工作量或人数 |
| ATL PC 审核及人工调整计划约 3 小时 → 20 分钟 | 本人确认包括审核与人工调整的环节时间变化，不等于模型求解或整个计划流程耗时 |
| 汇丰 98% | 客户状态识别的项目 benchmark；非制造良率、非全量生产保证 |

### 与旧简历的口径差异

原简历中的 “reduced planner workload by 90%” 不应继续按已实现收益复述。若面试官引用，可直接说：

> I should clarify that wording. The 90% referred to ATL’s planned reduction in PC staffing, rather than a verified reduction in workload or implemented headcount. The remaining staff were expected to focus on data maintenance and plan adjustments.

目前未修改已提交的简历；如需要后续投递版，可将该句改为客户计划/预期，并清楚标明是否实现尚未确认。

新的可陈述结果为 PC 审核及人工调整计划从约 180 分钟降至 20 分钟：减少约 160 分钟，约 88.9%。面试优先说原始时间，避免与拟减员 90% 混淆；该比例不能泛化为全部 PC 工作量下降。还需准备衡量范围、是否为同规模计划、典型值或平均值等追问。

## 12. 反问直属领导：优先选三题

> Which problem would you most want this person to solve in the first three to six months: ramp readiness, daily output, yield, test capacity, or labor efficiency?

目的：明确岗位当下的业务重点。

> How is ownership divided between this role and the process, test, quality, and CM engineering teams?

目的：确认本人是分析推动、项目执行，还是直接负责工艺/测试诊断与签核。

> For someone with my planning and optimization background, where would you see the strongest fit, and which hands-on skills would you expect from day one?

目的：具体讨论相关经验与必须立即具备的现场能力。适合在已经充分说明优势之后问，不在开场先要求对方评估全部不足。

备用：What does a typical week at the CM site look like for this role? / How do you verify that a corrective action has improved output or yield and remains effective?

## 13. 口语练习优先级

先练五题：自我介绍、松下成果、M6S 返工、IT 分歧、岗位匹配。每题先有 60–90 秒版本，再准备两层追问。

接着练五题：低产出、FPY 下滑、OEE、数据看板、工程变更。用“确认范围和指标 → 分解问题 → 与负责人验证 → 行动 → 效果复查”的逻辑回答，不用尚未做过的现场履历装饰。

英语卡住时可使用：

- Let me clarify the production constraint first.
- The key issue was not total capacity, but how the equipment was shared over time.
- My direct responsibility was the algorithm. Their team owned the application system.
- That was a planning result, not an actual shipment metric.
- I have relevant experience in planning, but I have not directly owned that process.
- I would work with the process and test owners to verify that hypothesis.

## 14. 最新补充事实与剩余细节

已确认：松下与 ATL 长期客户驻场、短时车间参观、主要透过 PC 理解生产、亲自做过生产任务安排；M6S 由 PC 审核；PC 审核及人工调整计划时间由 3 小时降为 20 分钟；ATL 维护输入，版本管理已落地。

本人进一步确认：PC 时间包括人工调整；此前所说排班指生产任务安排，并非人员排班；可以接受频繁出差。

可留作深入追问准备的细节：3 小时和 20 分钟对应的计划规模、是否为典型值或平均值；松下本人亲自实现与他人承担的模块；确认交期指标按订单还是数量统计。这些不会阻止当前稿件练习。

这些细节不会阻止当前练习。实际生产执行效果、直接工艺/测试/良率工程职责均不能由 PC 审核和驻场经历推导。

