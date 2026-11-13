# Meta 二轮面试：英文口述速记卡

适用：约 45 分钟英文面试，面试官为部门负责人。更新：2026-11-13。

这七张卡来自完整问答稿，优先用于录音练习。先看提示词回答，再对照正文；讲完后停下来。题目顺序只是练习安排，现场按面试官的问题选择内容。

[完整中英问答与三个项目介绍](C:/Users/HP/Desktop/application_material/meta/Meta_部门负责人面试_中英问答与三项目介绍.md)

每次回听检查：前 15 秒是否答题；个人贡献是否清楚；是否解释了判断；是否在结论之后结束。以下时长按每分钟 110–130 个英文词粗估，停顿会增加时间，以自己的录音为准。

## A01. Tell me about yourself. / 请介绍一下自己

提示词：OR background → HSBC → Panasonic / ATL / framework → contribution to this role

英文约 98 词；不含额外停顿约 45–53 秒。

> I’m Jinfeng. My background is in operations research, with a focus on manufacturing planning and resource allocation.
>
> At HSBC, I work on workforce capacity planning and case assignment. Previously, at Youhualin, I led a small algorithm team and worked on planning systems for Panasonic and ATL. I also led the algorithm workflow design for a reusable supply chain planning framework.
>
> My relevant experience combines optimization design with working alongside planners and IT teams. Based on the first interview, I see a clear contribution in reviewing vendor solutions, clarifying planning requirements, and helping resolve data and implementation issues.

## A02. Why are you interested in this role? / 为什么选择这个岗位

提示词：operations → vendor review → manufacturing data → technical judgment + delivery

英文约 94 词；不含额外停顿约 43–51 秒。

> The first interview helped me understand the role more clearly. It sits within operations and involves reviewing the scheduling vendor’s technical approach and coordinating planning data and system integration with manufacturing partners.
>
> I’m comfortable with that scope. My optimization background would help me evaluate assumptions, identify missing constraints, and discuss trade-offs with the vendor. My experience working with planners and IT teams would help me move issues toward resolution.
>
> My longer-term interest is in manufacturing planning. I see a clear way to contribute through technical judgment and cross-team delivery in this role.

## P1. Tell me about your most successful project. / 90–120 秒主介绍

提示词：customer-estimated savings → layered planning → procurement / planner handoffs → my role

英文约 158 词；不含额外停顿约 73–86 秒。

> One of my most successful projects was a production planning system for Panasonic Electronic Materials, where I led the algorithm solution. After deployment, changeovers decreased by about ten per month, representing approximately RMB 300,000 in estimated monthly cleaning-cost savings based on the customer’s calculation.
>
> The challenge was to reduce changeovers while coordinating materials, equipment, molds, and delivery commitments. I made two key design decisions.
>
> First, I used a layered approach. MRP selected relevant production routes and material alternatives before detailed resource planning. That reduced the combinations carried into the daily model.
>
> Second, I made the business handoffs explicit. Orders with material shortages needed procurement confirmation before delivery dates were quoted. Planners kept ownership of their relatively stable material calendar and selected the finished-goods quantities to send into detailed scheduling.
>
> I agreed on the design with the customer’s IT and planning teams. My contribution was connecting the optimization structure with the decisions and workflow that the customer needed.

## A09. Tell me about a time you aligned stakeholders with different priorities. / 如何协调不同目标的团队

提示词：three priorities → observe diagnosis → operational milestone → phased responsibilities → versioning implemented

英文约 137 词；不含额外停顿约 63–75 秒。

> At ATL, our algorithm team needed more reliable test data while keeping development effort under control. IT wanted direct database integration, and production planners wanted usable schedules as soon as possible.
>
> I invited the IT lead to observe how we diagnosed infeasibility and schedule defects. I also asked the planning lead to explain what still prevented schedules from being released to production. That helped us agree on the operational milestone.
>
> We agreed to keep versioned file inputs during debugging. IT would build the input interface and version management. Our team would work on algorithm quality and runtime, and start database adaptation after a limited rollout in Dongguan.
>
> Input version management was implemented, with ATL maintaining the inputs. My contribution was making the dependencies visible and agreeing on a sequence in which each team had a clear responsibility.

## A10. Tell me about a failure. / 介绍一次失败

提示词：PC found issue during rollout → I did not ask why → shared equipment → resource combinations → earlier scenario validation

英文约 136 词；不含额外停顿约 63–74 秒。

> One failure was in ATL’s M6S scheduling project. During rollout, the customer’s production planners identified a problem with how our schedules handled shared equipment.
>
> My mistake was in understanding the requirement. The planners had asked for machines to start and finish together as much as possible. I implemented that request without investigating the operational reason behind it.
>
> Winding machines shared supporting equipment that could not switch during a continuous batch. Encouraging synchronized starts and finishes did not fully capture that restriction.
>
> I revised the candidate batches to include compatible combinations of winding and supporting machines. The production planning team then reviewed the revised schedules.
>
> I learned to investigate the operating mechanism behind a user’s request. In a similar project, I would walk through a complete batch with planners and validate shared-resource use before rollout.

## T1. Tell me about a complex project you led. / 90–120 秒主介绍

提示词：Ningde scale → master / daily / correction → candidate expansion → capacity-margin trade-off → planner effort

英文约 163 词；不含额外停顿约 75–89 秒。

> At ATL, the main challenge was extending production scheduling from Dongguan to the much larger Ningde factory. The existing solution had daily scheduling, and I led important changes to its algorithm structure.
>
> I added a master-planning layer to allocate demand and capacity before detailed scheduling. Daily scheduling could then focus on continuous batches and machine combinations. I also added a correction layer to handle finer changeover and capacity effects while preserving the main schedule structure.
>
> To control model size, I designed an iterative approach that started with a sparse set of candidate batches and progressively added options based on the solve results.
>
> We kept some capacity margin in master planning so detailed schedules had room to work. That reduced the risk of overly tight allocations, but could increase changeovers.
>
> Later, planner review and manual adjustment time fell from about three hours to twenty minutes. My main lesson was to make the decision boundaries explicit and assess the final plan across the whole process.

## F1. Tell me about the integrated algorithm architecture. / 90–120 秒主介绍

提示词：engineer users → shared planning structure → workflow → solver adapter ownership → team efficiency

英文约 157 词；不含额外停顿约 72–86 秒。

> I led the algorithm workflow design for a shared supply chain planning framework. Its main users were algorithm engineers, especially those who needed to build a correct planning model without recreating the infrastructure for every project.
>
> The foundation was a discrete-time production planning model. MPS, MRP, and S&OP planning share material flows, inventory, demand, and production decisions across time. We reused that structure and expressed differences through capacity rules, constraints, objectives, and time granularity.
>
> The workflow covered data checks, shared domain objects, model construction, sequential objectives, solver integration, and result processing. Customer-specific rules could extend the input, model, or output layers.
>
> I personally designed and implemented the Gurobi and CPLEX adaptation layer, with an optional Pyomo path. The domain model was a shared effort, largely drawing on my earlier AUX work, and the product manager designed the product interfaces.
>
> The framework reduced repeated development and gave the team a common language for implementation, handovers, and reviews.

## 三个情景题：只记回答顺序

| 问题 | 英文提示顺序 |
|---|---|
| How would you evaluate the vendor? | operating decision → inputs / constraints / objectives → agreed test cases → baseline comparison → acceptance evidence |
| What if planners cannot use the schedule? | one concrete example → fixed input snapshot → data / model / post-processing → correction → final-plan validation |
| What if manufacturing data is unreliable? | affected decision → source / owner / unit / timestamp → checks → resolve gap or limit scope → owned temporary assumptions |

未来方法用 would。以上是方法提纲，完整英文回答见主稿 A06–A08。

## 三个可选反问

> What is the most important problem you would want this person to solve in the first six months?

> What would this role own in technical acceptance of the vendor’s solution?

> How do operations, manufacturing partners, and the vendor resolve disagreements about whether a schedule is usable?

## 需要卡住的事实口径

- Panasonic: RMB 300,000 per month is a customer-based estimate of cleaning-cost savings. 99.9% is a planning metric.
- ATL: three hours to twenty minutes refers to planner review and manual adjustment.
- M6S: PC found the issue during rollout. My error was not investigating the reason behind synchronized starts and finishes.
- Framework: I led the algorithm workflow and fully built the solver adaptation layer. The domain model was a shared effort; the PM designed product interfaces.
- M6S 的实际业务损失、修正耗时和具体 PC 验收步骤仍待补充；不要临场编造。

## 组织思路时可用的句子

> Let me give you the main point first.

> My specific responsibility was…

> I made two key decisions.

> The trade-off was…

> The result we could verify was…
