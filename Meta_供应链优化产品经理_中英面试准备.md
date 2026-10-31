# Meta：供应链与运筹优化产品经理面试准备（中英对照）

更新日期：2026-11-01。

## 先读这一页：这次应当如何定位

联系人称同一岗位有多个 HC，你所对应的方向更需要运筹优化与供应链背景；你理解 PM 是 Product Manager。因此，本稿按“面向制造与供应链业务的内部决策产品经理”准备。这是依据联系人信息与本人理解作出的准备假设，并非已经确认正式职位、组织分工或面试题型；开场或反问时可以自然核实。

主要任务是让面试官看到：你能够理解用户要做什么决策，把业务需求转化为数据、规则和优化能力，作出范围与优先级取舍，并与业务及工程团队一起把工具落地。

### 核心定位

> I bring operations research expertise and experience working with manufacturing planners. I can translate complex planning needs into clear decision rules and practical tools, while working with business and engineering teams to make them usable.

我具备运筹优化专长，以及与制造计划团队合作的经验。我能够把复杂的计划需求转化为清晰的决策规则和实用工具，并与业务、工程团队合作，让这些工具真正能够使用。

### 面试官应记住的四点

1. **理解用户与决策。** 能分清用户要解决的是缺料、交付承诺、产能配置还是详细任务安排。
2. **能作产品判断。** 能决定哪些约束必须体现、哪些细节可以分阶段处理，以及如何平衡效果、时效和维护成本。
3. **有跨团队交付经验。** 能协调 PC、客户 IT 和算法团队的不同诉求，明确数据接口与职责。
4. **能讨论实际效果。** 看用户审核和调整计划所需时间、实际业务结果与可解释性，不只看算法速度和目标函数。

### 五个案例的使用顺序

| 案例 | 产品经理视角 | 证据强度与边界 |
|---|---|---|
| 松下 | 用户需求、决策分层、目标取舍、业务价值 | 主导算法方案及业务调研；不扩展为正式拥有全部产品路线图 |
| ATL IT 输入版本 | 非功能需求、跨团队分歧、责任边界、工程落地 | ATL 维护输入，版本管理已落地；没有排障提速数字 |
| ATL M6S | 需求遗漏、产品可用性、用户反馈、修正与反思 | PC 审核，审核及人工调整从约 3 小时降到 20 分钟；不是产线实测结果 |
| 通用供应链框架 | 客户共性与个性、能力复用、技术平台演进 | 简历支持框架设计与指导工程师；没有正式商业路线图或收入数字 |
| 汇丰 | 统一数据定义、端到端决策链、AI 工作流 | 当前项目进行中；98% 是项目 benchmark，不是全量生产准确率 |

现场工程稿保留作领域补充；本次不将 FATP/SMT、OEE、良率工程作为主要经历证明。供应链深度重点是制造计划、物料与产能、MPS/APS/MRP/S&OP 相关算法能力，不自动扩大到采购商务、物流网络运营或供应商合同管理。

## 1. 英文自我介绍：约 90 秒

> Hi, I’m Jinfeng. My background is in operations research, with a focus on manufacturing planning and resource allocation.

你好，我是晋峰。我的背景是运筹优化，重点方向是制造计划与资源配置。

> I currently work at HSBC on a capacity planning product. Before that, I spent more than four years at Youhualin, where I led a small algorithm team and worked on manufacturing projects for Panasonic Electronic Materials and ATL.

我目前在汇丰参与产能规划产品。在此之前，我在悠桦林工作了四年多，带领小型算法团队，参与松下电子材料和 ATL 等制造业项目。

> My work has involved understanding user requirements, defining planning rules, designing optimization solutions, and working with business and IT teams. At Panasonic, I helped translate delivery priorities, material availability, and equipment constraints into different planning levels. At ATL, I worked on production scheduling and input version management with the customer teams.

我的工作包括理解用户需求、定义计划规则、设计优化方案，以及与业务和 IT 团队协作。在松下，我参与将交付优先级、物料可用性和设备限制转化为不同层次的计划方案。在 ATL，我参与生产排程，并与客户团队推动输入版本管理。

> I also designed a reusable supply chain planning framework. That experience made me think beyond solving one model, to which capabilities should be shared and which should remain customer-specific.

我还设计过可复用的供应链计划框架。这让我不仅关注一个模型怎样求解，也关注哪些能力应当共用，哪些应当保留为客户定制。

> I’m interested in a product role where I can combine this technical background with user understanding, prioritization, and cross-functional delivery to improve planning decisions.

我希望在产品岗位中，将技术背景与用户理解、优先级判断和跨团队交付结合起来，改善计划决策。

记忆顺序：背景 → 当前 → 制造用户与交付 → 可复用框架 → 为什么产品岗位。不要主动说自己已有正式 Product Manager 职位或完整商业产品经营责任。

## 2. 为什么适合产品经理，为什么从算法转向产品

### Q1. Why do you want to move into product management?

> What interests me most is helping users make better decisions. In my previous projects, choosing the right problem and clarifying the business rules were as important as the algorithm itself.

我最感兴趣的是帮助用户作出更好的决策。在过去的项目中，选对问题和明确业务规则，与算法本身同样重要。

> For example, at Panasonic we had to distinguish material shortages from resource constraints, and confirmed commitments from newly requested dates. These choices affected the value of the solution before we discussed the mathematical method.

例如在松下，我们需要区分缺料问题和资源限制，也需要区分已确认交期承诺和新增需求的期望日期。这些选择在讨论数学方法之前，就已经决定了方案的价值。

> I want to take more responsibility for understanding user needs, deciding what to build first, and following the result through to actual use. My optimization background helps me judge feasibility and trade-offs, while I continue developing broader product skills.

我希望更多地负责理解用户需求、决定先做什么，以及持续跟进产品的实际使用效果。优化背景帮助我判断可行性和取舍，同时我也会继续发展更全面的产品能力。

**重点：** 不是因为不想开发或协调，而是希望扩大从问题到使用效果的责任。正式路线图、产品发现、用户推广等职责如果过去没有独立承担，表达为希望进一步承担。

### Q2. You have not held a PM title. What relevant experience do you bring?

> My formal role was algorithm lead, not product manager. The relevant experience is that I worked directly with users on requirements, translated business needs into planning rules, made technical trade-offs, and coordinated with IT teams on delivery.

我的正式角色是算法负责人，并非产品经理。相关经验在于，我直接与用户沟通需求，将业务需求转成计划规则，作出技术取舍，并与 IT 团队协调交付。

> I also worked on reusable planning capabilities across customers. That gave me experience separating common needs from specific extensions. I would bring that foundation to the role, while being clear about which product responsibilities would be new for me.

我也参与了跨客户复用的计划能力建设，因此有区分共性需求与特定扩展的经验。我会把这些基础带到岗位中，也会明确哪些产品职责对我来说是新的。

**追问准备：** 哪些需求是你提出的？哪些是 PC 决定的？你是否有最终优先级决定权？预算和发布时间谁负责？没有正式决策权不妨碍讲清你如何提供依据并影响决定。

### Q3. Why Meta and this opportunity? Why leave HSBC?

> HSBC has broadened my experience in capacity planning and aligning data and business definitions across teams. I value that experience.

汇丰拓展了我在产能规划，以及跨团队统一数据和业务定义方面的经验，我很重视这些收获。

> My long-term interest is in manufacturing and supply chain decision-making. Based on what I understand about this opportunity, it could let me combine my optimization background with broader ownership of planning tools and cross-functional outcomes.

我的长期兴趣在制造与供应链决策。根据目前了解到的信息，这个机会可能让我把优化背景与更完整的计划工具责任、跨团队工作成果结合起来。

> I would like to understand which user decisions this role is expected to improve and where the team sees the biggest unmet need.

我也希望了解，这个岗位具体希望改善用户的哪些决策，以及团队认为当前最大的未满足需求是什么。

此稿不假设某个 Meta 内部计划产品已经存在，也不代写未体验过的智能眼镜产品经历。

## 3. 松下主案例：从用户问题到产品方案

### Q4. Tell me about a product-like initiative you led.

> A useful example is the planning solution for Panasonic Electronic Materials. The users were production planners. They needed to manage delivery commitments while dealing with material availability, equipment capacity, and mold constraints.

一个合适的例子是松下电子材料的计划方案。用户是生产计划员，他们需要在物料、设备产能和模具限制下安排生产，并管理交期承诺。

> I was the algorithm lead and worked with the planning team on requirements. A key decision was to distinguish different problems. Monthly supply-demand analysis identified material shortages and affected orders. Daily planning considered resource calendars, and short-term scheduling produced more detailed production arrangements.

我担任算法负责人，与计划团队一起梳理需求。关键判断是区分不同问题：月度供需分析识别物料缺口及受影响订单；日度计划考虑资源日历；短期排程形成更具体的生产安排。

> We also separated confirmed delivery commitments from newly requested dates. For mold planning, we balanced delivery priorities with the cost of changes, using optimization together with local calendar adjustments.

我们还区分了已确认交期承诺和新增需求的期望日期。针对模具安排，我们兼顾交付优先级与换型代价，将优化方法与局部日历调整结合起来。

> After deployment, mold changes decreased by around ten per month. Panasonic estimated the cleaning cost at RMB 30,000 per change, giving estimated monthly savings of about RMB 300,000. Over three months, the planning results showed 99.9% fulfillment against confirmed dates. That was a planning metric, not actual shipment performance.

上线后，每月换型减少约 10 次。松下测算每次清洗费用约 3 万元，因此月度清洗费用节约估计约 30 万元。三个月的计划结果中，确认交期满足指标为 99.9%；这是计划指标，并非实际出货表现。

> From a product perspective, the important part was matching different decisions to the right planning level, so the output addressed the users’ actual needs.

从产品角度，重要的是把不同决策放在合适的计划层次处理，使输出真正回应用户需求。

**故事拆解：** 用户是 PC → 问题是资源与承诺耦合 → 你负责算法方案与调研 → 产品判断是分层及优先级 → 结果是清洗费用估算和计划满足指标。

**不能扩写：** 已独立拥有整个产品路线图、采购与工厂协同已形成自动闭环、所有模型结果都在产线上验证、实际交付率达到 99.9%。

### Q5. How do you discover user needs?

> In Panasonic and ATL, I spent extended periods at the customer sites and worked mainly with production planners. That helped me understand how they made decisions and where planning rules became difficult.

在松下和 ATL，我长期在客户现场，主要与生产计划员合作，了解他们如何决策，以及计划规则在哪些地方变得复杂。

> For a new product, I would ask users to walk me through a real planning cycle: what starts it, what data they use, which decisions they make, where they make manual adjustments, and who approves the result. I would compare stated requirements with actual examples before defining the scope.

对于新产品，我会请用户带我走一遍真实计划周期：什么触发计划、用哪些数据、作哪些决定、在哪些地方人工调整，以及谁批准结果。在确定范围前，我会把口头需求与实际案例核对。

> My M6S experience showed why this matters: a requirement can look complete at the aggregate capacity level while still missing how shared equipment works over time.

M6S 经历说明了这件事的重要性：需求在总产能层面看似完整，却仍可能遗漏共享设备在时间上的实际使用方式。

前段是既有经历；“请用户走一遍完整周期”是建议方法，不声称所有项目都已采用正式访谈流程。驻场不等于长时间观察产线，本人直接工作是生产任务安排。

### Q6. How do you prioritize requirements and define an MVP?

> I would first agree on the user decision and the cost of getting it wrong. Then I would separate requirements needed for a valid decision from features that improve convenience or coverage.

我会先明确用户要作什么决定，以及决策错误的代价，再区分哪些要求是决定有效性的基础，哪些功能主要改善便利性或覆盖范围。

> For a scheduling product, a critical shared-equipment constraint may be required before the output can be used. A more detailed dashboard or support for every product family could come later. I would also consider frequency, business impact, data readiness, engineering effort, and dependencies.

对于排程产品，关键的共享设备约束可能是输出可用的前提；更丰富的看板或覆盖全部产品系列可以后续再做。我也会考虑使用频率、业务影响、数据准备程度、工程工作量和依赖关系。

> I would define the first release around a limited but complete workflow, with a named user, clear acceptance criteria, and a way to handle exceptions.

我会围绕一个范围有限但完整的工作流程定义首版，明确用户、验收标准及异常处理方法。

**追问：What would you leave out?**

> I would consider leaving out automatic execution, all-site coverage, and advanced optimization features until the core recommendations were useful and validated. I would not remove a critical feasibility or quality requirement just to meet a date.

在核心建议被验证有用之前，我会考虑暂不加入自动执行、全部工厂覆盖及高级优化功能；不会为了赶日期而删掉关键可行性或质量要求。

这是新产品的假设取舍，不把松下项目的实际迭代顺序改写成正式 MVP 路线图。

## 4. ATL 两个案例：交付与反思

### Q7. Tell me about influencing a cross-functional partner.

> At ATL, our team owned the optimization algorithm, while the customer’s IT team owned the application. Their IT lead preferred direct database input and was concerned about the work of preparing text files.

在 ATL，我方负责优化算法，客户 IT 团队负责应用系统。IT 负责人倾向算法直接读数据库，也担心准备文本输入会增加团队工作。

> My concern was preserving the exact input for each run. Optimization issues can take time to investigate, and changing data can make them hard to reproduce. I shared several real debugging examples to explain the requirement.

我关注的是保留每次运行使用的确切输入。优化问题排查耗时较长，如果数据变化，问题就难以复现。我通过几次真实排障案例分享说明这一需求。

> We kept file-based input, ATL maintained the input files, and version management was implemented with an input ID for each run.

最终保留了文件输入，由 ATL 维护，系统实现了版本管理，并为每次运行保留相应输入编号。

> The product lesson was to define the underlying requirement—reproducibility—rather than argue only about the implementation. It also required a clear boundary between the application team and the algorithm team.

产品上的体会是，应当明确底层需求——可复现性，而不只争论实现方式；同时需要明确应用团队和算法团队的责任边界。

**追问：Could a database solve that too?**

> Yes. A database could also support reproducible inputs through appropriate snapshot or versioning mechanisms. Our project used versioned files. The requirement was traceable input, not that every product must use files.

可以。数据库也可以通过合适的快照或版本机制支持输入复现。我们的项目采用版本化文件，核心要求是输入可追溯，而非所有产品都必须用文件。

**产品能力映射：** 非功能需求 → 利益相关方诉求 → 真实证据 → 职责与接口 → 落地。未提供的文件导出机制、维护成本数字和故障恢复 SLA 不补写。

### Q8. Tell me about a failure or a requirement you missed.

> In ATL’s M6S scheduling project, my initial model met aggregate capacity limits but missed how winding machines shared supporting equipment during a continuous batch. The equipment could not switch freely between batches, so the resulting plan could not be executed as intended.

在 ATL M6S 排程项目中，我最初的模型满足总产能限制，却遗漏了连续批次中卷绕机台如何共享旁工序设备。设备无法在批次之间自由切换，因此计划无法按预期执行。

> I corrected the candidate batches to include compatible combinations of winding and supporting machines. To control complexity, I used business experience to keep the more efficient combinations.

我修改了备选批次，将卷绕机台与旁工序设备的可行搭配组合纳入其中，并根据业务经验保留更高效的组合，以控制复杂度。

> The revised plan was reviewed by the production planning team. Their review and manual adjustment time went from about three hours to twenty minutes.

修正后的计划由 PC 审核。他们审核及人工调整计划的时间从约 3 小时降到了 20 分钟。

> The lesson was that a planning product must represent the user’s real operating constraints. For future work, I would validate representative production scenarios earlier and use this case as a regression test.

这让我认识到，计划产品必须体现用户真实的运行限制。在以后的工作中，我会更早验证有代表性的生产场景，并将这个案例作为回归测试场景。

最后一句是从经历推导的建议改进，使用 would；没有证据时不说已建立了完整回归体系。时间改善是项目后续结果，不证明只由这一次修正单独造成。

**追问：Who validated it?**

> The production planning team reviewed it. That supports the planning workflow result I described. It is different from claiming that every schedule was verified through actual production execution.

由生产计划团队审核。这支持我所说的计划工作流程改善，但与声称每份计划都经过实际生产验证不同。

## 5. 衡量价值、用户信任与技术取舍

### Q9. How would you measure the success of an optimization product?

> I would measure three levels: the business outcome, the user workflow, and the technical quality. A faster solver is useful only if it helps users make a better decision in time.

我会衡量三个层面：业务结果、用户工作流程和技术质量。求解器更快，只有在帮助用户及时作出更好决策时才有价值。

> For example, I would track the relevant cost or service metric, the time needed to review and adjust a plan, and whether recommendations are actually used. I would also track feasibility, runtime, data quality, and major exceptions.

例如，我会看相关成本或服务指标、审核和调整计划所需时间，以及建议是否真正被使用；同时跟踪可行性、运行时间、数据质量和重大异常。

> At ATL, the review and adjustment time decreased from about three hours to twenty minutes. At Panasonic, the cost estimate came from fewer mold changes. I would keep those definitions separate from planned staffing reductions or actual shipment performance.

在 ATL，审核与调整时间从约 3 小时降到 20 分钟；在松下，成本估算来自换型减少。我会将这些指标与拟定的人员减少目标、实际出货表现分别说明。

### 建议的验收指标，不是已承诺的 Meta KPI

| 层次 | 示例指标 | 需要约定的口径 |
|---|---|---|
| 业务 | 实际交付、清洗费用、缺料暴露提前量 | 计划还是实际、观察周期、分母、需求组合 |
| 用户 | 审核调整时间、例外处理时间、持续使用率 | 哪一步、是否含人工调整、哪些用户与计划 |
| 决策 | 可行方案比例、关键约束违背、计划稳定性 | 硬约束/软目标、固定范围、排除项 |
| 系统 | 端到端时延、数据新鲜度、运行失败率 | 不能用求解时限替代实测全流程时间 |

高采纳率不能单独证明建议质量；低人工修改率也可能来自缺乏修改能力。指标需结合用户反馈和业务结果。

### Q10. What if the algorithm looks good but planners do not use it?

> I would investigate the reason before changing the model. Users may distrust the data, see a missing constraint, disagree with priorities, or find that the output does not fit their workflow.

我会先调查原因，再决定是否改模型。用户可能不信任数据、发现缺失约束、不认同优先级，或觉得输出不适合自己的流程。

> I would review a real rejected recommendation with the user and trace the input, rule, and decision. Then I would separate a data issue, a modeling issue, and a workflow issue, and address the highest-impact cause first.

我会与用户一起查看一条真实被拒绝的建议，追溯输入、规则与决策过程，然后区分数据问题、模型问题和工作流问题，优先处理影响最大的原因。

> I would support understandable explanations and controlled adjustments, so users can see why a recommendation was made and what changes when they override it.

我会提供容易理解的解释和受控调整机制，让用户了解建议的原因，以及人工修改后会产生什么影响。

这是方法回答。不要将用户不采用直接归因于“不会用”或“抗拒变化”；先用 M6S 说明系统本身也可能漏掉关键规则。

### Q11. How would you decide between rules, optimization, and AI?

> I would start with the decision, not the technology. If clear rules solve the problem reliably, I would not add optimization just for complexity. Optimization is useful when scarce resources and competing objectives create important trade-offs.

我会从决策出发，而非技术出发。如果清晰规则已经能可靠解决问题，就不会为复杂而增加优化。资源稀缺和多个目标之间需要重要取舍时，优化更有价值。

> AI may help prepare unstructured information or explain outputs, but it should not silently replace verified business constraints. I would compare options on value, data needs, speed, explainability, and maintenance cost.

AI 可以帮助整理非结构化信息或解释结果，但不应在用户不知情的情况下替代已确认的业务约束。我会从价值、数据要求、速度、可解释性和维护成本比较不同方案。

### Q12. How do you balance solution quality and response time?

> I would ask how much time the user has to make the decision and what improvement is valuable. A daily planning workflow and an urgent exception may need different response times.

我会先了解用户有多少决策时间，以及多大改善才有价值。日常计划和紧急异常可能需要不同的响应速度。

> At ATL, sparse candidate batches and selective expansion helped control model size. At Panasonic, different planning levels addressed different decisions. These approaches involve trade-offs, so I would measure final feasibility and business quality along with runtime.

在 ATL，稀疏备选批次和选择性扩展帮助控制模型规模；在松下，不同计划层次处理不同决策。这些方法都有取舍，因此我会同时衡量最终可行性、业务质量和运行时间。

不要把启发式候选扩展说成严格列生成或全局最优保证，也不未经核实称所有工厂已经并行。

## 6. 可复用框架与 AI：体现产品化能力

### Q13. How would you turn customer projects into a reusable product?

> In the supply chain planning framework, I separated shared capabilities from customer-specific extensions. The shared foundation included data preparation, domain objects, model building, solving, post-processing, and KPI output.

在供应链计划框架中，我区分了共用能力与客户特定扩展。共用基础包括数据准备、领域对象、模型构建、求解、后处理和 KPI 输出。

> We used shared code and targeted extensions rather than copying a complete model for every customer. Standardized logs and intermediate results also helped diagnose issues across projects.

我们通过共用代码和有针对性的扩展支持客户差异，而非为每个客户复制完整模型。标准日志和中间结果也帮助跨项目排查问题。

> For a product roadmap, I would group requests by the underlying user problem and promote a capability into the core when it solves a recurring need. A rare rule could remain an extension. I would also consider configuration complexity and regression risk.

在产品路线图上，我会按底层用户问题归类需求；某项能力反复被需要时，再考虑纳入核心。少见规则可以保留为扩展，同时评估配置复杂度和回归风险。

前两段有简历依据；最后一段是对产品职责的建议做法。框架代码复用本身不证明做过付费产品定价、市场选择或正式路线图治理。

### Q14. How do you handle inconsistent data definitions?

> In my HSBC capacity planning project, I coordinate with teams to align definitions of demand, workload, productivity, capacity, and work in progress. Staff qualifications and eligibility rules also need to be consistent.

在汇丰产能规划项目中，我与不同团队协调需求、工作量、效率、产能和在制任务等定义，同时统一人员资格和任务承接规则。

> From a product perspective, those definitions are part of the decision contract. If different teams calculate capacity differently, a shared dashboard or optimizer can create misleading comparisons.

从产品角度，这些定义是决策约定的一部分。如果各团队计算产能的方式不同，共用看板或优化器就可能造成误导性比较。

> For a new tool, I would agree on the source, owner, unit, time window, and exception rules for each critical field before using it in decisions.

对于新工具，我会先约定关键字段的来源、负责人、单位、时间窗口和异常规则，再将其用于决策。

最后一段为建议方法；当前汇丰项目上线范围与业务效果未补充，不扩写为已经全面推广成功。

### Q15. How would you use AI responsibly in a planning product?

> At HSBC, I built Dify workflows to extract customer status and review information from unstructured notes. The outputs were validated before use in optimization. Customer-status identification achieved 98% accuracy on the project benchmark, which does not guarantee the same accuracy on all production data.

在汇丰，我通过 Dify 从非结构化记录中提取客户状态和审查信息，输出在进入优化前经过校验。客户状态识别在项目基准测试上达到 98% 准确率，但这不保证在所有生产数据上都有同样表现。

> For a planning product, I would use AI first where outputs can be checked, such as preparing draft structured information or summarizing exceptions. Important constraints and recommendations would remain traceable to verified data and rules, with access controls and human review appropriate to the decision.

对于计划产品，我会优先将 AI 用于输出可验证的环节，如生成结构化信息草稿或汇总异常。重要约束和建议仍应能追溯到核实后的数据与规则，并按决策要求设置访问控制和人工复核。

> I would measure the workflow benefit and the error types, not only a single accuracy figure.

我会衡量工作流程收益及错误类型，而非只看一个准确率数字。

生产环境访问控制等属于建议设计，不声称本人已完成 Meta 所需的全部 AI 治理工作。

## 7. 产品设计练习：供应链计划决策工具

### 题目（模拟，并非已知 Meta 面试题）

> Design an internal tool to help a hardware operations team respond to demand changes under material and capacity constraints.

设计一个内部工具，帮助硬件运营团队在物料和产能受限时应对需求变化。

### 回答步骤与可口述英文

**第一步：先澄清用户和决策。**

> I would first clarify who uses the tool and what decision they need to make. For this example, I’ll assume the primary user is a production planner deciding how to allocate limited supply over the next few weeks, with operations leaders reviewing major trade-offs.

我会先明确谁使用工具，以及需要作什么决定。在这个例子中，我先假设主要用户是决定未来几周有限供给如何分配的生产计划员，运营负责人审核重大取舍。

要问：范围是单厂还是多厂？决策是资源分配还是详细排程？目前最痛的是响应慢、信息不一致还是建议不可执行？需求变动与执行变更由谁批准？不要开场就列所有算法。

**第二步：定义用户流程。**

> The workflow would be: compare the new demand with the current plan, identify material and capacity gaps, evaluate a small set of response options, and let the authorized owner approve the change.

流程是：比较新需求与现有计划，识别物料和产能缺口，评估少量应对方案，再由有权限的负责人批准调整。

**第三步：限定首版。**

> For the first release, I would choose one product family and one planning scope. I would support a validated input snapshot, gap identification, scenario comparison, and planner review. Automatic release to execution and coverage of every factory could come later.

首版选择一个产品系列和一个明确计划范围，支持经过校验的输入快照、缺口识别、情景比较和计划员审核。自动下发执行及全部工厂覆盖可以后续考虑。

数据包括：需求与承诺日期、库存和在途物料、BOM 与供应路径、设备日历与有效产能、已冻结任务、必要资质或切换限制。具体以选择的决策粒度确定，不自动声称所有数据都已存在于 MES。

**第四步：明确取舍与例外。**

> The decision policy would need to be agreed with business owners. For example, protect confirmed commitments before evaluating new requests, while showing cost, inventory, and disruption implications. If the current constraints cannot satisfy demand, the tool should show the gap rather than silently relax a critical rule.

决策规则需要与业务负责人约定，例如先保护已确认承诺，再评估新需求，并展示成本、库存和扰动影响。若现有限制下无法满足需求，工具应显示缺口，而非悄悄放松关键规则。

这是情景假设，不代表任何团队都必须采用该排序。区分物理硬约束、批准后可改变的资源条件，以及业务软目标。

**第五步：定义结果和验证。**

> I would measure review and adjustment time, major feasibility errors, and whether users can make the required decision in time. I would compare representative cases with the current process, use planner review, and separate planned service metrics from actual execution outcomes.

我会衡量审核调整时间、重大可行性错误，以及用户是否能及时完成所需决策。用代表案例与当前流程比较，通过计划员审核，并区分计划服务指标和实际执行结果。

试点先确定输入版本、基线、同类场景与例外反馈；不要承诺用未经设计的简单 A/B 就能隔离供应链网络中的全部因果影响。

### 假设首版需求单：练习交付物，不是过去写过的 PRD

| 项目 | 内容 |
|---|---|
| 用户 | 单一范围内的生产计划员；运营负责人审核重要方案 |
| 痛点 | 需求变化后，人工核对供需和资源影响慢、难以解释取舍 |
| 决策 | 哪些需求能满足，缺口在哪里，哪些响应动作值得批准 |
| 范围 | 输入校验、版本快照、缺口追溯、情景比较、人工审核 |
| 首版暂缓 | 全工厂推广、自动执行、所有复杂优化特性 |
| 功能验收 | 可追溯到数据与规则；明确缺口和假设；保留人工修改记录 |
| 质量保障 | 关键约束校验、不可行解释、失败状态可见、原流程可继续 |
| 业务验收 | 与业务约定审核时间和决策质量的基线；试点后再定推广阈值 |

## 8. 交付、优先级与推广：补充高频追问

### Q16. What if stakeholders disagree about priorities?

> I would make the competing goals explicit and use a concrete scenario to show the consequences of each option. I would distinguish a constraint required for valid output from a preference that can be traded off.

我会明确冲突目标，用具体场景展示不同选择的后果，并区分保障输出有效性的必要限制和可以取舍的偏好。

> If the disagreement affects business commitments, I would bring it to the responsible decision owner with a recommendation. I would record the decision and its assumptions so engineering and users work from the same policy.

若分歧影响业务承诺，我会向有决策权的负责人提出建议，并记录决定和假设，让工程与用户遵循一致规则。

可接 ATL IT 的真实故事作证。没有独立最终拍板权，不说“我决定所有优先级”。

### Q17. How would you manage a release when a dependency is late?

> I would clarify what is blocked and whether it prevents a safe, useful release. I would discuss the options with the dependency owner: reduce scope, change the sequence, or move the date.

我会明确受阻内容，以及它是否妨碍安全且有用的交付，再与依赖方讨论缩范围、调整顺序或修改日期。

> Any temporary workaround would need clear ownership, quality checks, and a removal plan. I would communicate the impact early rather than hide a missing dependency behind an apparently complete release.

临时方案需要明确负责人、质量检查和后续移除计划。我会尽早沟通影响，避免让缺失依赖被表面完成的发布掩盖。

目前没有本人明确的延期交付故事，以上保留为方法回答；不编造通过压缩工期按时发布的案例。

### Q18. How would you roll the product out to more sites?

> I would compare which parts of the workflow and rules are shared and which are site-specific. A successful pilot is useful evidence, but it does not prove the same model works unchanged everywhere.

我会比较哪些流程和规则是共通的，哪些是工厂特定的。试点成功是有用证据，但不能证明同一模型可以不变地用于所有地方。

> I would validate data readiness, local constraints, ownership, and acceptance criteria at the next site. I would reuse the core capabilities, isolate necessary extensions, and monitor adoption and exceptions after rollout.

我会在下一处核实数据准备、当地限制、职责和验收标准；复用核心能力、隔离必要扩展，并在推广后监控使用和异常。

与通用框架连接，但不声称已经负责所有客户现场推广、培训和商业交付。

### Q19. What would you do in your first 90 days?

> In the first month, I would learn the users, current planning workflow, decision rights, and data landscape. I would agree with my manager on the problem worth owning and a measurable baseline.

第一个月，了解用户、现有计划流程、决策权限和数据状况；与直属领导确认值得负责的问题及可衡量基线。

> In the second month, I would define a limited use case with business and engineering partners, validate representative scenarios, and agree on the initial scope and acceptance criteria.

第二个月，与业务和工程伙伴定义有限用例，验证代表性场景，约定首版范围和验收标准。

> In the third month, I would aim for a reviewed prototype or pilot if data and engineering readiness allow it. The next step would depend on user feedback and measured results, not a fixed promise to launch everywhere.

第三个月，若数据和工程条件允许，争取完成经审核的原型或试点。下一步由用户反馈和实测结果决定，不预先承诺全面上线。

这是初步建议，实际时间与范围要按团队现状调整。

## 9. 必须保留的事实口径

| 内容 | 正确表述 | 避免说成 |
|---|---|---|
| 正式角色 | 运筹科学家、算法负责人/工程师，小团队指导经验 | 已任正式 PM、拥有全部路线图与预算 |
| 松下 30 万元/月 | 每月少约 10 次换型，客户按每次清洗 3 万元估算 | 财务审计确认的总成本净收益 |
| 松下 99.9% | 三个月的确认交期计划满足指标 | 实际出货率、良率 |
| ATL 3 小时 → 20 分钟 | PC 审核及人工调整计划时间 | 算法运行时间或所有计划工作总工时 |
| ATL 90% | 计划部门拟减少的 PC 人员比例，执行未确认 | 已实现的人数或工作量下降 |
| ATL 输入版本 | ATL 维护，版本管理已实施 | 只有口头建议，或本人开发全部前后端 |
| 驻场 | 长期客户驻场，主要与计划员合作 | 长期直接负责 SMT/FATP 工艺、良率或设备调试 |
| 供应链 | 制造计划、物料/产能、MPS/APS/MRP/S&OP 相关能力 | 所有供应链职能均有实操，完整 S&OP 管理机制由本人运营 |
| 汇丰 98% | 项目 benchmark 的客户状态识别准确率 | 全量生产表现、制造质量指标 |

S&OP 不只是一个优化模型，MRP 也不等于具体机台排程。讨论系统能力时，说明本人负责的算法部分与业务管理流程如何分工。

## 10. 反问面试官：优先问职责与成功标准

> From what I understand, this opening may include different responsibilities. For the position we are discussing, would the main ownership be an internal planning product, a set of optimization capabilities, or broader operational execution?

根据我的理解，这次招聘可能包含不同职责。我们讨论的这个位置，主要负责内部计划产品、一组优化能力，还是更广泛的运营执行？

> Who are the primary users, and which decisions are hardest for them today?

主要用户是谁？目前哪些决策对他们最困难？

> What would success look like in the first six months, and how would you measure it?

前六个月怎样算成功？团队如何衡量？

> How are product priorities decided between operations, data, and engineering teams? What decisions would this role own directly?

运营、数据和工程团队之间如何决定产品优先级？这个岗位直接拥有哪些决策权？

> What tools and planning processes already exist, and where do you see the biggest gap?

已有工具和计划流程是什么？目前最大的缺口在哪里？

现场选两三题，不逐一问完。先自然核实产品职责，避免开场称“我知道这个岗位不做现场工作”，因为这点尚未确认。

## 11. 面试前复习顺序与词汇

### 最先练熟的六题

1. 90 秒自我介绍。
2. 为什么适合 Product Manager：经历相关，但不改写正式职位。
3. 松下：用户、决策、取舍、结果。
4. ATL IT：可复现输入与版本管理。
5. ATL M6S：遗漏需求、修正、PC 审核调整时间。
6. 如何确定 MVP 与衡量产品价值。

### 练习标准

每个故事先准备 60–90 秒，再留两层追问。完整松下可讲约 2 分钟。先说用户和决定，再展开技术；每个建议方法用 would，每个既有事实用过去时。模拟题按“用户—问题—范围—方案—取舍—验证”组织，不强背框架名称。

| 英文 | 中文 |
|---|---|
| user workflow | 用户工作流程 |
| decision support | 决策支持 |
| prioritization / trade-off | 优先级判断 / 取舍 |
| minimum viable product (MVP) | 最小可行产品，首版应能完成一个有限的有效流程 |
| acceptance criteria | 验收标准 |
| adoption | 实际采用/持续使用 |
| non-functional requirement | 非功能需求，如性能、可复现性和可靠性 |
| input snapshot / traceability | 输入快照 / 可追溯性 |
| hard constraint / soft objective | 硬约束 / 软目标 |
| scenario comparison | 情景比较 |
| product roadmap / dependency | 产品路线图 / 依赖关系 |
| shared capability / customer extension | 共用能力 / 客户扩展 |

### 可直接记住的五句话

> I would start with the user’s decision, not the algorithm.

我会从用户要作的决策出发。

> A feasible model is useful only if the output fits the real workflow.

模型可行，还需要输出适合实际工作流程才能发挥价值。

> The requirement was reproducibility; the versioned file was our implementation.

需求是可复现性，版本化文件是当时采用的实现方式。

> I would separate business impact, user effort, and technical performance.

我会分别看业务影响、用户投入和技术表现。

> My previous title was algorithm lead, but my work included requirements, trade-offs, and cross-functional delivery.

我之前的职称是算法负责人，但工作包含需求梳理、取舍与跨团队交付。

## 12. 资料依据与阅读说明

- 本人简历、前述面试指南及对话中确认的项目事实；数字以本稿第 9 节为准。
- 本稿的 Product Manager 定位来自联系人描述及本人理解，没有将此前现场工程 JD 认定为已正式改写。
- 内部决策产品、MVP 与 90 天计划是针对本次定位设计的准备建议，并非已发生的本人经历或已知 Meta 团队规划。
- 产品管理涉及用户、业务和技术协同的一般背景可参考 [Atlassian Product Management](https://www.atlassian.com/agile/product-management)。这不是 Meta 的职责定义。
- 供需与产能计划的通用问题范围可参考 [Microsoft Master Planning](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-planning-home-page)。本稿不假设 Meta 使用该产品，也不将其功能当作本人已实现的功能。
