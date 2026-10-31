# Meta Reality Labs Initial IC：陈述方向与关键问答

准备日期：2026-10-29。历史通用初稿，已由《Meta_直属领导英文面试准备_岗位定制版.md》替代。请优先使用新版，其中已加入完整 JD、ATL 真实分歧与 M6S 返工案例。

**事实修订，以本段及新版为准：** 松下清洗费用由松下测算，每次换型约 3 万元；99.9% 是三个月的计划结果，非实际交付。ATL 的 90% 是计划部门拟减少的 PC 人员比例，不是已实现的工时或人数下降。本稿下方未核实模板与旧口径仅保留作准备过程记录，不能直接用于面试。

## 1. 本稿的依据和适用范围

- 以本目录 `Jinfeng_Qiu_Manufacturing_Operations_Resume_261018.docx` 为主要履历依据，参考英文简历文本和现有 HR 准备稿。
- 面试要求以 `RL Operations - Initial (IC).pdf` 为准：与工程负责人交流约 45 分钟，重点涉及 Scalability and Scope、XFN Collaboration，以及背景、兴趣和职业目标。
- 现有 HR 资料写明目标岗位为 Manufacturing Operations Engineer、Reality Labs / Smart Glasses；尚未收到本次完整 JD，因此岗位职责与评价权重仍待核实。
- 参考了相邻 DJI 目录中的松下和 ATL 技术准备笔记。它们记录的是此前静态代码分析的结论，不等于本轮重新审查了源代码，也不能独立证明现场收益。
- 以下题目是根据指南和个人经历推演的练习题，不是 Meta 官方题库。英文为建议表达；涉及实际行为的表述须本人核实。

## 2. 面试的主要陈述方向

### 核心定位

我擅长理解复杂制造流程，把订单承诺、物料和资源限制转化为清晰的运营决策，并与生产计划团队合作，形成可执行、可解释的方案。

> My strength is turning complex manufacturing constraints into practical planning decisions. I combine operations research with a clear understanding of business priorities and close collaboration with production teams.

要让对方记住四件事：

1. 能从业务决策出发：先明确交付承诺、资源瓶颈和成本，再选择建模方式。
2. 能处理规模与复杂度：分层规划、候选筛选、局部修复，平衡细节、速度和计划质量。
3. 能让不同团队协同：澄清指标、日期口径、资格与规则，推动形成共同认可的决策依据。
4. 能说明成果与边界：区分个人贡献与项目整体结果、估算与实测、计划满足率与实际交付率。

### 案例安排

| 案例 | 主要证明什么 | 推荐展开内容 | 必须补足 |
|---|---|---|---|
| 松下 CCL | 制造理解、技术判断、业务取舍、与 PC 合作 | 承诺交期与期望日期；月度缺料分析、日度资源计划、短期 APS；模具日历修复；炉批表达 | 一次真实分歧、团队分工、收益口径 |
| ATL | 规模化、连续生产、多层计划、复杂度控制 | 主计划与日计划；连续生产区间；稀疏候选与按需扩展 | 本人具体负责模块、规模耗时、90% 工时口径 |
| 汇丰 | 跨团队规则统一、信息不完整下推进 | demand/workload/capacity/WIP 定义；人员资质与跨市场限制；中期计划与日常分配 | 一个真实规则分歧、当前上线范围与实际效果 |
| 通用供应链框架 | 将一次交付变成可复用能力 | 公共模型与客户扩展、标准输入输出、日志与诊断、指导初级工程师 | 具体复用项目、本人设计与他人实现边界 |
| 中石油 | 技术深度备用 | 非凸物理约束、线性近似、可行性修复、效率验证 | 同数据同精度基准；不主动占用制造主线时间 |

### 每段经历都按这条线说

业务目标 → 最难的限制 → 我的职责 → 两三个关键判断 → 如何与他人推进 → 结果及验证 → 反思。

先用 90 秒至 2 分钟讲完整故事，再按追问展开。技术方法每次都连接一个业务目的。例如：“分层是为了分清缺料和资源配置问题”；“局部修复是为了在时效要求内改善模具安排”。

## 3. 英文自我介绍：约 75–90 秒

> Hi, I’m Jinfeng. My background is in operations research, with a focus on manufacturing planning and resource allocation.
>
> I currently work at HSBC on operational capacity planning. Before that, I spent more than four years at Youhualin, where I led a small algorithm team and worked on manufacturing planning projects.
>
> One example was Panasonic Electronic Materials. I worked with the production planning team to understand delivery priorities, material constraints, and equipment and mold capacity. I led the algorithm solution design, using different planning levels to address different decisions.
>
> I also worked on battery production scheduling at ATL, where production continuity and model size were important challenges.
>
> Across these projects, my strength has been understanding the business problem, making practical technical trade-offs, and turning the results into plans that users can work with.
>
> I’m interested in this opportunity because I want to apply that experience more directly to manufacturing operations and continue building my knowledge of the production process.

中文逻辑：现在做什么 → 相关制造经验 → 松下、ATL 的代表性难点 → 可迁移能力 → 职业动机。完整 JD 确认前，不把特定现场职责说成已经掌握。

## 4. 松下主案例：约 2 分钟

### 中文陈述方向

这个项目面向松下电子材料的覆铜板生产，难点在于订单交期、材料可用性、干燥与成型工序、设备模位及模具套数相互影响。减少换模有助于降低费用，但过度集中生产也可能影响交付。

我的职责是算法方案负责人，与生产计划团队调研需求、设计方案，并指导算法工程师开发。进一步说明本人亲自实现的模块、其他工程师负责的部分，以及上线验收由谁推动，待本人补充。

方案中的三个关键判断：

1. 区分订单日期与承诺。已确认订单与新需求使用不同的日期口径和优先级，避免只用统一权重掩盖业务承诺。
2. 区分计划层次。月度供需分析识别物料缺口及受影响订单；日度计划考虑具体设备、模具与日历；短期 APS 形成炉批等执行对象。
3. 选择混合方法。用模型暴露模具能力缺口，再在局部窗口检查模具套数、已有工单搬迁及交付影响，调整日历后重新求解。

结果部分根据简历陈述：上线后每月换模减少约 10 次，按每次 3 万元估算，月度清洗费用节约约 30 万元。项目记录的确认交期满足指标为 99.9%。在确认统计口径前，不把该指标表述为全部订单实际按时交付率。

### 英文口述稿

> One project I would highlight is the planning and scheduling solution for Panasonic Electronic Materials.
>
> The challenge was that delivery commitments, material availability, equipment capacity, and mold availability were closely connected. Reducing mold changes could lower cleaning costs, but we also had to protect delivery priorities.
>
> As the algorithm lead, I worked with the production planning team on requirements and led the solution design.
>
> There were three important decisions. First, we distinguished confirmed delivery commitments from newly requested dates. Second, we used separate planning levels: monthly supply-demand analysis, daily resource planning, and short-term scheduling. Third, we combined optimization with local adjustments to mold calendars, rather than putting every detailed decision into one large model.
>
> The short-term scheduling results were then converted into furnace batches and sub-batches for users.
>
> According to the project results reported in my resume, mold changes decreased by around ten per month. At an estimated cleaning cost of RMB 30,000 per change, that represented about RMB 300,000 in estimated monthly savings.
>
> The main lesson for me was to connect technical decisions to business priorities and the way planners actually use the output.

练习时可将 “According to…” 简化为 “After deployment…”，但应先确认数字来源和本人观察范围。99.9% 暂留作追问，口径确认后再加入主稿。

## 5. 关键问题及回答

### Q1. What was the most difficult technical decision you made?

考察：技术判断和取舍，不能只列模型名称。

中文方向：选松下，解释为何没有把半年所有细节塞进一个模型；说明分层降低复杂度，但层间可能存在偏差，仍需验证短期可执行性。

> A difficult decision was choosing how much detail to include at each planning level. A very detailed model could represent more rules, but it would also be harder to solve, maintain, and explain.
>
> I separated material shortage analysis from detailed resource planning. For mold-calendar decisions, I combined optimization with local adjustments and re-solving.
>
> This made the problem more manageable, but it also meant we had to pay attention to consistency between planning levels. I would not describe the approach as a guarantee of global optimality.

追问准备：被简化的具体规则是什么？为什么允许？哪项规则绝不能简化？请用本人真实决定补强。

### Q2. How did you make the solution scalable?

中文方向：ATL 回答“如何控制问题规模”，通用框架回答“如何支持更多客户与工程师”。

> At ATL, one challenge was the number of possible production intervals. Enumerating every possible interval would make the model too large.
>
> I worked on an approach that started with a smaller candidate set and selectively expanded it around unmet demand. We also separated higher-level allocation from detailed scheduling.
>
> The trade-off was between search coverage and computational effort. This was a practical candidate-expansion method, rather than a claim that we had searched every possible schedule.

如本人确认是独立设计，可把 “I worked on” 改成 “I designed”。准备一组真实数据量、前后耗时和解质量；没有数据时不要编倍数。已有 ATL 笔记提醒：候选扩展不等于严格列生成，工厂分块不自动等于已实现并行。

### Q3. Tell me about a disagreement with a stakeholder.

现有材料不足以写真实成稿，必须本人补充。不要将技术上的交期与换模权衡自动编成真实人际冲突。

回答结构：

1. 对方职责和目标：为什么其要求合理？
2. 具体分歧：哪一项规则、指标或优先级不一致？
3. 我的动作：澄清顾虑、比较方案、用什么证据讨论？
4. 达成决定：谁决定、怎样记录、谁执行？
5. 结果：分歧如何解决，是否仍有代价？

英文填空框架，填完事实后才能使用：

> In [project], [stakeholder] wanted [A], while [another stakeholder / I] was concerned about [B].
>
> My responsibility was [scope]. I first clarified [underlying concern]. Then I [specific action], using [evidence or comparison].
>
> We agreed on [decision and ownership]. The result was [verified outcome]. I learned [specific lesson].

避免：“我说服他们算法更好”“我们沟通了一下就解决了”。面试官需要看到对方立场和你的推进动作。

### Q4. How do you handle unclear or inconsistent requirements?

中文方向：汇丰最合适。不同团队说的 capacity、productivity、WIP 未必同义；先统一定义及资格限制，再讨论配置方案。

> In my HSBC project, a key part of the work has been aligning definitions across teams. Demand, workload, productivity, and capacity need consistent meanings before the planning results can be compared.
>
> I coordinate with teams to standardize these definitions and staff eligibility rules. The planning then connects demand and workload to staffing, scheduling, and case assignment.
>
> My main point is that consistent business definitions are part of the solution itself. They determine whether the output supports a valid operational decision.

必须补一个具体例子：究竟哪个定义不同，造成什么决策偏差，你如何推动确认。目前不要虚构跨市场上线成果。

### Q5. How did you validate the solution and manage risk?

这是高概率追问；简历未充分描述实际验证流程。下面是方法回答，不能直接声称所有项目都已完整执行。

> I separate model quality from operational readiness. A solver returning a solution is only one part of the check.
>
> I would check material balance, resource capacity, delivery priorities, and whether post-processing changes the feasibility of the plan. I would also review representative outputs with the planning team and compare the key metrics using consistent definitions.
>
> For a live process, I would agree on exception handling and a fallback with the operational owner before relying on the output.

实际案例版本需补：谁做 UAT？测了哪些场景？如何处理超时或不可行？是否有试运行和回退？上线后谁监控？没有做过的步骤用 “I would”，做过且能解释的步骤才能用 “I did”。

### Q6. What was your personal contribution?

中文方向：明确“我负责什么”“我亲自做什么”“团队整体交付什么”。

> In the Panasonic project, I was responsible for the algorithm solution design and technical guidance. I worked with the production planning team to translate requirements into planning rules and supported the other algorithm engineers.
>
> The overall system and its business results were team outcomes. My direct contribution was [specific design, module, implementation, and decision]. Other team members were responsible for [their scope].

方括号必须补实。还需说明自己是否负责接口、部署、验收和现场支持，不能由“算法负责人”自动推出。

### Q7. Tell me about a failure or a decision you would change.

必须选真实事件，暂不编完整故事。候选方向：业务规则理解偏差、过细模型拖慢求解、后处理暴露不可执行安排、指标定义不一致；只有确实发生过才能使用。

结构：我的判断 → 产生的问题 → 如何发现 → 如何补救 → 后来改变的工作方式。

> I initially [decision], because [reason]. We later found [specific problem]. I took responsibility for [my part] and [corrective action]. The result was [outcome]. Since then, I [concrete change to my process].

避免把“太追求完美”当失败；不把团队或客户当作唯一原因。

### Q8. You have limited direct CM experience. Why are you a good fit?

> My direct experience is in manufacturing planning and optimization, rather than owning a contract manufacturer's daily operations.
>
> The relevant experience I bring is understanding production constraints, working with planning teams, and balancing capacity, materials, changeovers, and delivery commitments. Panasonic and ATL gave me practical experience with these decisions.
>
> I would need to build more depth in the specific assembly, testing, quality, and partner-management processes of this role. I would do that by working closely with the factory and engineering teams, learning the process, and taking ownership of a clearly defined operational problem.

中文要点：明确直接经验 → 两个项目作证 → 具体学习范围与行动。不要只用“学习能力强”作保证，也不主动认领良率工程、SMT/FATP、NPI 或供应商商务谈判经历。

### Q9. Why Meta, and why move from HSBC?

> HSBC has broadened my experience in capacity planning and aligning business rules across teams. I value that experience.
>
> Over time, I have become clearer that I want to build my long-term career around manufacturing operations. I particularly enjoy working on problems where capacity, materials, and production decisions come together.
>
> Based on what I understand about this opportunity, it would allow me to bring my planning and optimization experience closer to manufacturing decisions, while developing deeper knowledge of the product and production process.

中文要点：已有收获 → 长期方向 → 岗位契合。具体对 Meta 的兴趣在 JD 和个人动机确认后补充，不代写并未体验过的产品经历。不把离职原因写成“不愿做数据清洗和跨部门协调”，因为目标岗位同样需要这些工作。

### Q10. Why an IC role after leading a team?

> My previous lead role combined technical guidance with hands-on problem solving. I still enjoy understanding the details, designing the solution, and working directly with users.
>
> What matters most to me is the scope and impact of the problems I can own. An IC role is attractive if it allows me to take responsibility for meaningful operational problems and work across teams to solve them.

该回答以本人确实愿意做 IC 为前提。领导小型算法团队是影响力证据，不要让对方误以为你只想分派工作、不愿亲自分析和跟进。

### Q11. What would you do if production were behind plan?

假设题，下面是建议方法，不是本人既有现场履历，也不假定目标工厂的具体流程。

> First, I would confirm the size of the gap, the affected products, and the delivery commitments at risk.
>
> Then I would work with the factory and engineering owners to identify the main constraint: material availability, equipment downtime, labor, yield loss, or scheduling.
>
> I would compare recovery options based on realistic capacity, qualified resources, material availability, quality requirements, and delivery impact. With the owners, I would agree on the action, responsibilities, and review timing.
>
> I would track whether the action actually restores output and update the plan as conditions change.

追问准备：提前启动、加班、转线、调整产品组合各有什么前提？哪些行动需要质量与工程确认？不要在根因不明时直接回答“优化排程就能解决”。

### Q12. How do you know the project created business value?

> I try to connect the result to a measurable operational outcome and make the definition clear.
>
> For example, the Panasonic result in my resume includes around ten fewer mold changes per month. The RMB 300,000 figure is an estimate based on RMB 30,000 per cleaning event.
>
> For delivery metrics, I distinguish requested dates from confirmed dates. I would also explain the reporting period, the included orders, and whether the metric describes the plan or actual execution.

最后一句表达应有的解释标准，不能替代实际统计证据。口径不确定时可说：

> I’d like to be precise: the figure was reported in the project results, but I would need to confirm the exact measurement basis before calling it an actual shipment performance metric.

更好的做法是面试前补全口径，再用确定的事实回答。

## 6. 必须准备的技术追问卡片

### 松下

- 为什么月模型放开标准资源产能？答：用于供需与缺料诊断；有限资源安排在后续阶段。不称月模型已完成有限产能交期承诺。
- 缺料订单怎样处理？现有笔记提示日模型存在过滤缺料需求逻辑；要核实这些订单是否仍计入最终交期 KPI 分母。
- 为什么混合 MIP 与启发式？答：用模型协调供需，用局部候选控制换模组合复杂度。局部选定后重求解，因为会影响其他订单和资源。
- 连续区间数量是否等于物理换模次数？答：它是代理指标；边界条件及实际清洗事件需另核实。
- MPS 与 APS 是否自动反馈？现有笔记仅确认分别存在入口；没有接口与现场证据时不称已形成自动闭环。
- 后处理是否会破坏可行性？可能改变取整、资源占用与时间安排；必须说明真实做过的最终校验，不能只引用原模型约束。

### ATL

- 候选扩展是不是严格列生成？现有笔记未见基于对偶价格和 reduced cost 的定价子问题，宜称“稀疏候选与业务驱动的增量扩展”。
- 多工厂是否并行？简历写有并行，现有笔记指出所见代码分块顺序运行。须确认部署版本与外部调度；未确认前说“分解为工厂级规划问题”。
- 分钟级求解对应什么？准备真实订单/PN/设备数、规划期、硬件、端到端耗时、解质量。不把参数时限当实测时间。
- 90% 减少的是什么？待核实人工排程时间、某步骤工作量或整体工时；不能说成产量提升 90% 或计划员人数下降 90%。

### 汇丰与复用框架

- 98% 准确率对应哪个任务、样本数和类别？是否独立测试集、如何处理边界样本？不能由 benchmark 推出全量生产准确率。
- AI 输出如何进入优化？简历写有规则校验、测试、人工复核；须说明本人实际执行的流程与责任人。
- 通用框架哪些部分复用、哪些客户定制？用一个真实差异说明，避免说成任意工厂都无需改动。

## 7. 数字核对表

| 简历数字 | 当前可说的范围 | 仍需确认 |
|---|---|---|
| 松下 7,000–10,000 订单、10,000+ 物料 | 六个月规划范围的项目规模 | 哪层模型、版本、实际数据批次 |
| 每月减少约 10 次换模 | 简历报告的上线后变化 | 前后周期、订单组合、是否持续 |
| 每次 3 万元，月度约 30 万元 | 10 × 3 万元的清洗费用节约估算 | 测算人、费用构成、实际与估算区别 |
| 确认交期 99.9% | 项目记录的确认交期满足指标 | 计划/实际、分子分母、周期、缺料订单 |
| 客户期望日期超过 90% | 与确认交期不同的项目指标 | 同上，不能混用 |
| ATL 计划员工作量减少 90% | 简历报告的工作量变化 | 哪项活动、基线工时、样本和测量人 |
| 汇丰客户状态识别 98% | 项目 benchmark 的准确率 | 样本、划分、标签、类别、生产表现 |
| 天然气多个场景超过 10 倍提速 | 特定全国网络测试与所述基准比较 | 同精度、同硬件、端到端范围 |

## 8. 推荐反问：选 2–3 个

> What are the most important operational problems you would want this person to own in the first six months?

前六个月最需要这个人负责解决哪些运营问题？

> How is responsibility shared between this role, manufacturing partners, and the engineering teams?

这个岗位、代工伙伴和工程团队如何分工？

> When capacity, delivery, and quality priorities conflict, how does the team make decisions?

产能、交付和质量优先级冲突时，团队如何作决策？

> Where would planning and optimization experience be most useful, and which hands-on manufacturing skills are essential from day one?

计划与优化经验在哪些方面最有价值？哪些现场制造技能是入职时就必须具备的？

## 9. 练习顺序

1. 先练自我介绍、松下两分钟主稿、为何岗位适合自己。
2. 为松下准备三层深度：90 秒业务概述、3 分钟决策与取舍、按追问展开模型和验证。
3. ATL 用于规模化；汇丰用于规则统一；框架用于复用能力。不要每题都重新从松下背景讲起。
4. 补齐一段真实分歧和一段真实失败，能够回答“你具体说了什么、做了什么、别人怎样回应”。
5. 每次口述后检查：是否说清个人职责、是否解释为何如此决策、数字是否有边界。
6. 45 分钟仅作练习节奏：开场约 2 分钟、项目与追问约 25–30 分钟、动机与匹配约 5 分钟、反问约 5 分钟；现场由面试官安排。

## 10. 等待本人补充

- 完整 JD、是否仍为智能眼镜 Manufacturing Operations Engineer、面试语言/时间/面试官职务。
- 松下或 ATL：一次真实分歧、具体推进动作、本人和团队职责划分。
- 松下成本及交期指标来源；ATL 90% 的统计范围。
- 一次真实失败、返工或上线后修正，以及处理结果。
- 对 Meta/产品/岗位的个人兴趣与长期目标；离开汇丰的真实原因是否与建议稿一致。

收到补充后优先修订 Q3、Q5、Q6、Q7 与成果段，将模板替换为可追问的真实故事，再压缩为口语卡片。
