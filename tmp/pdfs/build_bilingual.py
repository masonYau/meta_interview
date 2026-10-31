from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'output' / 'pdf'
OUT.mkdir(parents=True, exist_ok=True)
pdfmetrics.registerFont(TTFont('Chinese', 'C:/Windows/Fonts/simhei.ttf'))
pdfmetrics.registerFont(TTFont('Latin', 'C:/Windows/Fonts/arial.ttf'))

# Each block retains the original English and is followed by its Chinese translation.
blocks = []
def add(en, zh, kind='body'):
    blocks.append((kind, en, zh))

add('Reality Labs - Operations (IC)\nInitial Interview Guide', 'Reality Labs - 运营岗位（IC）\n初轮面试指南', 'title')
add('English / Chinese', '中英逐段对照版', 'sub')
add('Terminology: IC = Individual Contributor; XFN = Cross-functional.', '术语说明：IC 指个人贡献者（非管理岗）；XFN 指跨职能。', 'note')
add('Welcome to your preparation guide for your interview at Meta! This guide will take you approximately 15 minutes to review. Use the table of contents below to quickly jump to the section you are looking for. Whether you’re taking your initial screen or your full loop interview, our Operations leaders and recruiters put together this guide so you know what to expect and how to prepare. We recognize that interviewing can be stressful, so we hope this guide provides the information and resources you need. Remember, your recruiter is there to support you, so please reach out to them with any questions.', '欢迎阅读 Meta 面试准备指南！阅读本指南大约需要 15 分钟。你可以通过下方目录快速找到所需章节。无论你即将参加初轮筛选面试，还是完整的一轮面试流程，我们的运营团队负责人和招聘人员都希望通过本指南，帮助你了解面试内容及准备方法。我们理解面试可能令人紧张，希望这里的信息和资源能为你提供帮助。请记住，招聘人员会为你提供支持；如有任何问题，请随时联系他们。')
add('What you’ll find in this guide', '本指南内容', 'heading')
add('Accommodations process\nTeam introduction\nInterview process overview\nFinal tips for your interview\nPost interview - What to expect\nAppendix / Resources', '合理便利安排申请流程\n团队介绍\n面试流程概览\n面试前的最后建议\n面试后的安排\n附录与资源')
add('Accommodations process', '合理便利安排申请流程', 'heading')
add('Meta is committed to providing reasonable support (called accommodations) in our recruiting processes for qualified candidates with disabilities, physical conditions, mental health conditions, neurodivergence, sincerely held religious beliefs, pregnancy, childbirth, or related medical conditions, as required by law. If you need assistance or require an accommodation, reach out via the Accommodations request form.', 'Meta 致力于依法在招聘过程中，为符合岗位条件且有以下情况的候选人提供合理支持，即“合理便利安排”：残障、身体状况、心理健康状况、神经多样性、真诚信奉的宗教信仰、怀孕、分娩或相关医疗状况。如果你需要协助或合理便利安排，请通过“合理便利安排申请表”提出申请。')
add('Team introduction', '团队介绍', 'heading')
add('The Strategy & Operations team is the centralized hub for all strategy and operations for product, engineering, and the business teams. This team partners with leadership to help them grow, scale, and run their organizations effectively and make the most strategic decisions possible.', '战略与运营团队是产品、工程及业务团队开展战略与运营工作的集中枢纽。团队与管理层合作，帮助他们有效发展、扩大和管理组织，并尽可能作出具有战略价值的决策。')
add('Interview process overview', '面试流程概览', 'heading')
add('This guide will explain what to expect during your interviews with Meta. As part of your interview, you will have the opportunity to meet with peers, cross-functional partners, and other leaders at Meta. Your recruiter will be your guide throughout the process and aim to adequately prepare you to bring your best self to your interview.', '本指南将介绍你在 Meta 面试中可以预期的内容。面试过程中，你将有机会与未来的同事、跨职能合作伙伴以及 Meta 的其他负责人交流。招聘人员会全程为你提供指导，帮助你充分准备，在面试中展现最佳状态。')
add('What will your interview process be?', '面试流程是怎样的？', 'sub')
add('Your initial screen will consist of a 45-minute discussion with an engineering leader and will cover the breadth of your technical expertise and provide insight into domain specificity. This will be a conversation in which your interviewer will ask you questions that will allow you to drive the conversation.', '初轮筛选面试是一次与工程团队负责人的 45 分钟交流，将涵盖你技术专长的广度，并深入了解你在具体领域的专业能力。面试官会通过提问，让你有机会主导和展开讨论。')
add('During this conversation, we know you’re also trying to determine whether Meta is right for you and is this the right next step in your career. Your interviewer will spend time seeking to understand your interests, and will dedicate time to answering your questions, aiming to provide insight into a career path at Meta.', '我们知道，在交流中你也在判断 Meta 是否适合自己，以及加入 Meta 是否是职业发展的合适下一步。因此，面试官会花时间了解你的兴趣，并留出时间回答你的问题，帮助你了解在 Meta 的职业发展路径。')
add('• Cross-functional Collaboration\n• Assess ability to work with colleagues from other disciplines as peers\n• Be prepared to discuss your previous work', '• 跨职能协作。\n• 评估你能否以平等合作的方式，与其他专业领域的同事共事。\n• 请准备好讨论你过去的工作经历。')
add('Video Conference interview best practices', '视频面试建议', 'sub')
add('• Make sure you\'re in a quiet environment.\n• Double check that you have a reliable internet/phone connection.\n• It\'s okay to ask the person you\'re speaking with to speak slowly if you can\'t catch what they\'re saying.', '• 确保自己处于安静的环境中。\n• 再次检查网络或电话连接是否稳定可靠。\n• 如果听不清对方说的话，可以请对方放慢语速。')
add('You\'ll need a laptop with a webcam, speaker, and mic. We recommend using a headset or headphones with a mic for better quality audio, but this is optional.', '你需要一台配有摄像头、扬声器和麦克风的笔记本电脑。为获得更好的音频效果，建议使用带麦克风的耳机，但这不是硬性要求。')
add('While we embrace the usage of advanced tooling in our day-to-day work to build the future of social connection, we ask that you not use any unauthorized outside assistance during interviews. Throughout the interview process you may be asked to share your screen via Zoom. Here you can find guidance on how this works. Additionally, we ask that you disable and not use filters during your interview. This will help us get an understanding of how you approach problem-solving and coding independently. Outside assistance includes, but is not limited to, consulting external resources, seeing help from others, or using AI tools, like ChatGPT.', '虽然我们在日常工作中积极使用先进工具，打造社交连接的未来，但面试期间请勿使用任何未经授权的外部帮助。面试过程中，你可能需要通过 Zoom 共享屏幕，可参考相应操作指南。此外，请关闭滤镜，并在面试期间保持关闭。这有助于我们了解你独立解决问题和编写代码的方式。外部帮助包括但不限于：查阅外部资料、寻求他人帮助，以及使用 ChatGPT 等 AI 工具。')
add('For your interview, ensure Zoom screen sharing is enabled in advance, as setup may require a few minutes. Here\'s how: Enable Zoom screen share.', '请在面试前确认 Zoom 屏幕共享功能已启用，因为设置可能需要几分钟。操作方法见“启用 Zoom 屏幕共享”链接。')
add('A filter is considered any tool/feature that applies visual effects to your video feed, including virtual/blurred background.', '“滤镜”指对视频画面添加视觉效果的任何工具或功能，包括虚拟背景和背景模糊。')
add('Interview Dress Code', '面试着装', 'sub')
add('As you’re probably aware, we promote a casual environment at Meta so that everyone can be their authentic selves. Formal dress is not required (jeans are definitely ok!). Dress comfortably. We care about what you can do, not what you wear.', '你可能已经知道，Meta 提倡轻松随意的工作环境，让每个人都能展现真实的自己。面试不要求正装，穿牛仔裤完全没问题！穿着舒适即可。我们关注的是你的能力，而不是你的穿着。')
add('Initial Interview Overview', '初轮面试概览', 'heading')
add('What can you expect?', '你可以预期哪些内容？', 'sub')
add('This part of your discussion will focus on sharing real examples of high stakes projects you’ve led, indexing on technical experience and stakeholder management.', '这一部分的讨论将聚焦于你曾主导的重要、高风险项目的真实案例，重点考察技术经验和利益相关方管理能力。')
add('What do we look for?', '我们看重什么？', 'sub')
add('Your interviewer will be thinking about how your skills and experience might help Meta. During your initial screen, your interviewer will seek to understand your skills by assessing three focus areas:', '面试官会思考，你的技能与经验可以如何帮助 Meta。初轮筛选面试将围绕以下三个方面了解你的能力：')
add('Scalability and Scope: How do you design impactful solutions that account for scale, efficiency and XFN needs? How do you define requirements, identify, and mitigate potential risks?', '可扩展性与项目范围：你如何设计有影响力的解决方案，同时兼顾规模、效率与跨职能需求？你如何定义需求、识别潜在风险并降低风险？')
add('XFN Collaboration: How do you form collaborative partnerships with a wide range of stakeholders and manage challenging relationships? How do you work through differences and drive solutions that address issues while considering others’ perspectives, needs, and goals?', '跨职能协作：你如何与不同的利益相关方建立合作伙伴关系，并处理具有挑战性的合作关系？你如何化解分歧，在考虑他人的观点、需求和目标的同时，推动能够解决问题的方案？')
add('Additionally, your interviewer will take time to understand your unique background, expertise, interests, and career goals. They will also provide insights into the benefits of an engineering career at Meta in terms of potential career growth and opportunities to influence critical project work.', '此外，面试官会花时间了解你独特的背景、专业能力、兴趣和职业目标，并介绍在 Meta 从事工程相关工作的优势，包括潜在的职业成长空间，以及参与并影响关键项目的机会。')
add('How to prep', '如何准备？', 'sub')
add('Questions will be behavioral in nature, focused on asking you to describe a specific situation, the role you played, and the outcome.', '面试将以行为类问题为主，要求你描述一个具体情境、你在其中承担的角色，以及最终结果。')
add('Consider high impact projects you’d like to share, emphasizing the scope of the project and decision making.', '思考你想分享的高影响力项目，重点说明项目范围和决策过程。')
add('Consider your preferred domain expertise and what excites you about it.', '思考你最希望发挥的专业领域，以及这个领域为什么令你感兴趣。')
add('Consider situations where you’ve collaborated with a diverse group of 3 stakeholders to drive projects to completion. A significant portion of the conversation will be around how Meta fits your needs and areas of interest.', '回顾你与由三位不同背景的利益相关方组成的小组合作、推动项目完成的经历。交流中也会有相当一部分时间用于讨论 Meta 如何契合你的需求和兴趣。')
add('Translator’s note: “3 stakeholders” is reproduced as written in the source.', '译注：原文写有“3 stakeholders”，此处保留“三位”的表述。', 'note')
add('Prepare questions to gauge how your unique expertise can be utilized at Meta.', '准备一些问题，帮助你判断自己的独特专长可以如何在 Meta 发挥作用。')
add('Consider career experiences you’d like to have and prepare questions to understand how Meta fits into your goals.', '思考你希望获得哪些职业经历，并准备问题，了解 Meta 如何帮助你实现这些目标。')
add('Final tips for your interview', '面试前的最后建议', 'heading')
add('Be yourself. This means being open and honest about your successes and ways you’ve improved throughout your career. Also, be sure to call out how you have specifically added value to your team or projects you’ve contributed to. We value teamwork and what each individual member brings to the table.', '做真实的自己。坦诚分享职业生涯中的成就，以及你在哪些方面有所成长。同时，明确说明你具体为团队或参与的项目创造了什么价值。我们重视团队合作，也重视每位成员的独特贡献。')
add('Carefully review and familiarize yourself with the job description and perform research on Meta and the role. Be prepared to answer why you are interested in this specific role and in working at Meta.', '仔细阅读并熟悉职位描述，了解 Meta 和该岗位。准备好说明，你为什么对这个具体岗位感兴趣，以及为什么希望加入 Meta。')
add('Please take the time to review our mission statement and core values. These values influence how we work together to fulfill our mission to build the future of human connection and the technology that makes it possible. We also encourage you to take time using our technologies such as Facebook, Instagram, Messenger, and WhatsApp.', '花时间了解我们的使命宣言和核心价值观。这些价值观影响着我们的合作方式，帮助我们共同实现使命：构建人与人连接的未来，以及让这一切成为可能的技术。我们也鼓励你体验 Facebook、Instagram、Messenger 和 WhatsApp 等产品。')
add('One important piece of advice for your interviews: it’s ok if you don’t know! No one who works at Meta is an expert in all things, and we don’t look for perfection in the people we interview. If you aren’t sure of something during your interview, you’re encouraged to ask clarifying questions and be upfront if there are topics that you have less experience with.', '一条重要的面试建议：不知道也没关系！Meta 没有人精通所有事情，我们也不会要求候选人完美无缺。如果面试中遇到不确定的内容，可以提出澄清问题；对于经验较少的领域，也请坦诚说明。')
add('Prepare thoughtful questions for the interviewer(s). Your interviewer may challenge your ideas, and you should be ready to speak not only to what you recommend or have experienced but the why as well. It is important to think outside the box and to approach problems from creative and different perspectives.', '准备有深度的问题。面试官可能会挑战你的观点，因此你不仅要能说明自己的建议或经历，也要解释背后的原因。跳出惯常思路，从有创造性和不同的角度分析问题十分重要。')
add('Post interview - What to expect', '面试后的安排', 'heading')
add('You can expect your recruiter to provide a specific timeline or updates along the way. Your recruiter will inform you of next steps after your interview as soon as they are available. Feel free to follow up with them if you have not heard within a week of your interviews.', '招聘人员会向你提供具体时间安排，或在流程中持续更新进展。一旦面试后的下一步安排确定，他们会尽快告知你。如果面试结束后一周仍未收到消息，可以主动联系招聘人员跟进。')
add('Appendix / Resources', '附录与资源', 'heading')
add('Below is a curated list of resources to get started and help you prepare.', '以下精选资源可帮助你开始准备。')
add('Product Overviews', '产品介绍', 'sub')
add('Meta Quest 3\nMeta Quest Pro\nRay-Ban Meta Smart Glasses', 'Meta Quest 3\nMeta Quest Pro\nRay-Ban Meta 智能眼镜')
add('Additional Resources', '其他资源', 'sub')
add('Reality Labs\nMeta Connect 2023\nIntroducing Meta: A Social Technology Company\nEnsuring an Open and Interoperable Metaverse', 'Reality Labs\nMeta Connect 2023\n认识 Meta：一家社交科技公司\n确保元宇宙开放且互联互通')
add('Meta resources', 'Meta 相关资源', 'sub')
add('About Meta website\nMeta Newsroom website\nMeta Careers website\nCulture at Meta website\nMeta employee benefits website\nInterviewing at Meta: The keys to success blog', 'Meta 官方介绍网站\nMeta 新闻中心\nMeta 招聘网站\nMeta 企业文化网站\nMeta 员工福利网站\n《在 Meta 面试：成功的关键》博客文章')
add('Update personal information, track interview progress, and send thank you notes.', '更新个人信息、跟踪面试进度，以及发送感谢信。', 'sub')
add('At any time during the interview process, you can track your progress, send thank-you notes and update your personal information all via the Career Profile. If you do not receive a link from recruiting, you may create one.', '在面试流程的任何阶段，你都可以通过候选人个人主页（Career Profile）查看进度、发送感谢信并更新个人信息。如果招聘团队没有向你发送链接，你也可以自行创建个人主页。')
add('Thank you for taking the time to review this guide!', '感谢你花时间阅读本指南！')

links = {
'Accommodations request form':'https://www.metacareers.com/profile/accommodations_request/',
'Enable Zoom screen share':'https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0060596',
'mission statement':'https://about.meta.com/company-info/?utm_source=about.facebook.com&utm_medium=redirect',
'core values':'https://www.metacareers.com/facebook-life/',
'Meta Quest 3':'https://www.meta.com/quest/quest-3/',
'Meta Quest Pro':'https://www.meta.com/quest/quest-pro/',
'Reality Labs':'https://www.meta.com/emerging-tech/?utm_source=about.meta.com&utm_medium=redirect',
'Meta Connect 2023':'https://www.metaconnect.com/en/home',
'Introducing Meta: A Social Technology Company':'https://about.fb.com/news/2021/10/facebook-company-is-now-meta/',
'Ensuring an Open and Interoperable Metaverse':'https://about.fb.com/news/2022/05/ensuring-an-open-and-interoperable-metaverse/',
'About Meta website':'https://about.meta.com/',
'Meta Newsroom website':'https://about.fb.com/news/',
'Meta Careers website':'https://www.metacareers.com/',
'Culture at Meta website':'https://www.metacareers.com/facebook-life/',
'Meta employee benefits website':'https://www.metacareers.com/benefits',
'Interviewing at Meta: The keys to success':'https://www.metacareers.com/life/interviewing-at-facebook-the-keys-to-success',
'Career Profile':'https://www.metacareers.com/signup/?no_r=0',
}
def fmt(s, link=False):
    s = escape(s).replace('•', '-').replace('\n', '<br/>')
    if link:
        for label, url in sorted(links.items(), key=lambda x: -len(x[0])):
            if label == 'Reality Labs' and s != label:
                continue
            s = s.replace(escape(label), '<link href="'+escape(url, {'"':'&quot;'})+'" color="#1262A3">'+escape(label)+'</link>')
    return s

styles = {
'en':ParagraphStyle('en',fontName='Latin',fontSize=9.7,leading=14,textColor=colors.HexColor('#263445'),spaceAfter=5),
'zh':ParagraphStyle('zh',fontName='Chinese',fontSize=10.3,leading=16,wordWrap='CJK',textColor=colors.HexColor('#182A3C'),spaceAfter=13),
}
story=[]
for kind,en,zh in blocks:
    if kind in ('heading','sub','title'):
        size={'title':21,'heading':14,'sub':11.5}[kind]
        s1=ParagraphStyle('h_en',parent=styles['en'],fontSize=size,leading=size*1.25,textColor=colors.HexColor('#1262A3'),spaceBefore=13,spaceAfter=4)
        s2=ParagraphStyle('h_zh',parent=styles['zh'],fontSize=size if kind!='title' else 19,leading=size*1.35,spaceAfter=10)
        s1.keepWithNext=True
        s2.keepWithNext=True
        story.extend([Paragraph(fmt(en),s1),Paragraph(fmt(zh),s2)])
    else:
        en_s=styles['en']; zh_s=styles['zh']
        if kind=='note':
            en_s=ParagraphStyle('note_en',parent=en_s,fontSize=8,leading=11,textColor=colors.grey)
            zh_s=ParagraphStyle('note_zh',parent=zh_s,fontSize=8.5,leading=13,textColor=colors.grey)
        story.append(KeepTogether([Paragraph(fmt(en,True),en_s),Paragraph(fmt(zh),zh_s)]))

def footer(c, doc):
    c.setStrokeColor(colors.HexColor('#DCE4EC')); c.line(45,39,550,39)
    c.setFont('Latin',8); c.setFillColor(colors.HexColor('#64748B'))
    c.drawString(45,26,'Meta Reality Labs | Initial Interview Guide | EN / ZH')
    c.drawRightString(550,26,str(doc.page))

grouped=[]
pending=[]
for item in story:
    if isinstance(item, Paragraph) and getattr(item.style, 'keepWithNext', False):
        pending.append(item)
    elif pending:
        grouped.append(KeepTogether(pending + (item._content if isinstance(item, KeepTogether) else [item])))
        pending=[]
    else:
        grouped.append(item)
grouped.extend(pending)
story=grouped
target=OUT / 'RL Operations - Initial (IC) - 中英对照.pdf'
doc=SimpleDocTemplate(str(target),pagesize=(595.28,841.89),leftMargin=45,rightMargin=45,topMargin=34,bottomMargin=53,title='Reality Labs Operations (IC) - English / Chinese',author='')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(target)
