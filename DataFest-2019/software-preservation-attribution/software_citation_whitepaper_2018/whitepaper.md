# Software Citation Implementation in Astronomy

_A White Paper Summarizing Perceptions from the 2018 AAS Splinter Meeting on Implementing the FORCE11 Software Citation Principles_

**Daina Bouquin**, Harvard-Smithsonian Center for Astrophysics, Cambridge, MA

Daniel S. Katz, University of Illinois Urbana-Champaign, Urbana, IL

Edwin Henneken, Harvard-Smithsonian Center for Astrophysics, Cambridge, MA

August (Gus) Muench, American Astronomical Society, Washington, DC

Katie Frey, Harvard-Smithsonian Center for Astrophysics, Cambridge, MA

Arfon M. Smith, Space Telescope Science Institute, Baltimore, MD

Contact: daina.bouquin@cfa.harvard.edu

## Introduction

Software citation is foundationally important to the future of astronomy. Deep intellectual contributions are being made by people creating software to enable scientific research, and it is essential that software creators are encouraged to create these valuable resources. Efforts to help authors receive proper academic credit will allow them to prioritize writing software valuable for the astronomy community within their current profession or the ability to focus their whole career on it. With these facts in mind, on January 11, 2018 a &quot;splinter meeting&quot; was held at the 231st Meeting of the AAS that focused on implementing the FORCE11 Software Citation Principles ([Appendix A](https://github.com/CfA-Library/Cite_Astro_Software/blob/master/whitepaper.md#appendix-a)) in Astronomy. The goal of the splinter meeting was to gather feedback from astronomers, developers, and others whose expertise could inform the creation of resources to support the implementation of those principles. The meeting organizers aimed to identify some of the social and technical hurdles that affect software citation practices in astronomy and to understand factors that distinguish it from other fields where software citation is increasingly essential.

The purpose of this document is to summarize the perceptions expressed during the splinter meeting, and to define a few concrete next steps that can be taken to lower perceived barriers. This is not a comprehensive list of all topics discussed by all attendees at the meeting, but will hopefully serve to instigate further discussion and invite disruptive ideas about how to best share increasingly complex, continually changing, digital research artifacts like software.

**Structure of the Meeting**

Attendees were organized into five groups of five to seven people before the session began to ensure that each discussion group was made up of people representing a mix of relevant perspectives. The goal was to have representation by software authors, developers, journal editors, indexers, and librarians in each group to the extent that this was possible.

The splinter meeting at AAS was 90 minutes long, beginning with three brief presentations: an update about the current FORCE11 Software Citation Principles Implementation Working Group<sup>[1](https://www.slideshare.net/danielskatz/software-citation/danielskatz/software-citation)</sup>; the diversity of software being produced by the astronomy community<sup>[2](https://stsci.app.box.com/s/ooamf3ds1fxcqq7nnhgpnbjgi0sra031)</sup>; and the on-going Asclepias project<sup>[3](https://drive.google.com/file/d/1LB1arge6mMSHz1Lgxu6wn8Nr-Rb1LYNw/view?usp=embed\_facebook)</sup> from the AAS. A grant from the Alfred P. Sloan Foundation to the AAS for the Asclepias project  was used to fund the splinter meeting.

Attendees were given prompts ([Appendix B](https://github.com/CfA-Library/Cite_Astro_Software/blob/master/whitepaper.md#appendix-b)) after the presentations and asked to discuss the issues outlined within the prompts. A scribe at each table took notes about the ensuing conversation and presented highlights from the discussion at the end of the meeting.

## Recurrent Themes from Discussion Groups

**Motivations for Software Citation in Astronomy**

The FORCE11 Software Citation Working Group identified four primary motivations for developing the software citation principles in 2016: 1) the need for a complete record of the research process; 2) the need to enable software discoverability; 3) the importance of research reproducibility; and 4) the need to give credit to academic researchers of all levels for the software that they develop<sup>[4](https://doi.org/10.7717/peerj-cs.86)</sup>. Throughout the splinter meeting, the discussion groups eventually all came to focus predominantly on what was perceived as the primary motivating factor for implementing the principles in astronomy: giving credit for research software. The groups framed their conversations and focused the majority of their discussion around perceived social and technical barriers that impact people&#39;s ability to give and receive credit for their code. Therefore, credit and the lack of credit academics receive for their software became the driving force behind subsequent discussions. This is not to say that the other motivations were not seen as important to attendees, rather that less discussion in this meeting was linked to discoverability, research reproducibility, or completeness of the scientific record than to credit.

**Credit Leaves Many Questions Unanswered**

 By focusing on credit for academic researchers, issues surrounding authorship, native software citation, and subsequently the complexity authorship takes on in the context of software versioning came to the front. When authorship changes from one version of software to the next, the community highlighted how opaque attempts to implement the principles become. Specifically, the following questions remained unanswered:

1. Who is a software &quot;author&quot;? The astronomy community doesn&#39;t agree on how much someone should contribute to a code before that person is considered an author. This is true independent of version, but becomes an increasingly complicated discussion when multiple versions are being cited as contributors change over time. 
   1. Authorship questions highlighted a limitation that software papers present, as it was noted repeatedly that when a software paper exists, astronomers will overwhelmingly cite the paper rather than natively citing code regardless of whether or not the code they want to cite is the same version as the code discussed in the software paper. This may contribute to software paper authors receiving disproportionate amounts of credit and current contributors not receiving any. This preference for papers also runs counter to the FORCE11 Principle aiming for native software citation.
   1. There was also discussion about how to give acknowledgement for contributions that might not fit a definition of &quot;authorship&quot; and how giving all contributors equal credit as authors may serve to dilute the perceived importance of authoring software from external perspectives (e.g. tenure committees, funders, etc.).
      1.  The meeting attendees saw this issue (and also item 1.i.) as something that could be addressed through education and outreach to external groups, but that a concerted effort would be required from allies within those groups.
2. What should be cited to properly give author(s) credit? The ways in which astronomers are able to share software are varied (e.g. Zenodo record, AAS software paper, JOSS paper, ASCL record, etc.) and one piece of software may be represented as multiple digital objects (i.e. both as a paper and with a natively citable DOI from Zenodo) each with a different authorship list. More specifically, the following questions came up regularly in this context:
   1. When more than one digital object exists, what is the best way to give credit?
      1. How should we determine this?
      1. Knowing native software citation is the goal, should one also cite a software paper if one exists?
      1. How do we deal with multiple forks?
   1. Where should researchers look to find preferred citations?
      1. How can indexes support researchers looking for preferred citations?
   1. How should authors determine the preferred citation for their code?
      1. Where should an author make this information apparent (i.e. CITATION.md file<sup>[5](https://www.software.ac.uk/index.php/blog/2017-12-12-standard-format-citation-files)</sup>)?
   1. How should citations be calculated across different types of digital objects and versions of those objects?
      1. Should citations be aggregated?
      1. Should transitive credit be used in this context<sup>[6](http://arxiv.org/abs/1407.5117)</sup> or approaches described in the &quot;Metrics Toolkit&quot;<sup>[7](http://www.metrics-toolkit.org/citations-software/)</sup>?
3. What metadata do people need to make available to create a proper citation?
   1. Should metadata associated with the use of the code be put in the same place as the metadata required to document the creation of the code? Where should usage metadata be documented?
      1. Facilitating code reuse, although not as essential as credit from the meeting attendees perspective, should be encouraged. Metadata needed for reuse may be far beyond what is needed for a citation though.
   1. Should software papers require a structured metadata file to improve machine-readability (i.e. CodeMeta.json<sup>[8](https://github.com/codemeta/codemeta/blob/master/codemeta.json)</sup>)?

**Limited Situational Awareness**

Outreach was another perceived barrier that came up throughout the discussions. Specifically, attendees expressed that outside of the group gathered for the splinter meeting and a few other select groups within the broader astronomy community, there was very little situational awareness about the importance of software citation. For the purposes of this summary, a person with a high degree of situational awareness in the context of research software citation is a person capable of understanding how implementation of the FORCE11 Software Citation Principles will impact them, both immediately and in the future. Situational awareness of this sort came up in two contexts:

1. A lack of situational awareness pertaining to software citation by the community at large. This type of awareness was discussed as primarily a social issue in that this lack of awareness could be at least partially addressed through an awareness campaign.
   1. Attendees at the splinter meeting expressed that the Astronomy community as a whole may not possess an intuitive understanding of the importance of thinking critically about how and when to cite software and may not fully understand what they should be doing if they want people to cite their own software. As a result, it is not obvious to the community the ways in which research software deviates from a digital object like a research article or image.
      1. This lack of awareness may lead to apathy among members of the community who are not seeking credit for their software.
         1. Apathy may also stem from the misperception that software presents unresolvable problems for scholarly communication rather than being representative of issues that need to be addressed for all digital objects.
      1. Limited awareness about the importance of software citation may exacerbate the problem of software not being seen as a scholarly contribution by external groups (e.g. tenure committees, funders, etc.).
         1. Power dynamics can also prevent software authors from pushing back against these perceptions or pushing for software citation to be part of any formal curriculum or policy discussion.
   1. A noted lack of awareness was also discussed when splinter meeting attendees touched on publisher&#39;s editorial practices.
      1. Meeting attendees discussed the need for more targeted education on software citation best practices for reviewers and the need for more qualified referees.
2. Uncertainty about expectations from both the community and publishers perspective. The below questions about expectations could also be clarified through an awareness campaign and specific guidelines:
   1. What level of support is expected from software authors who share their code? (e.g. Code reuse in new contexts?; Feature requests?; Documentation?)
   1. What is the expectation of &quot;code quality&quot;? (i.e. Is &quot;hacky&quot; code something that should be shared?)
   1. Should scripts be shared or only packages that are meant to be reused?
      1. If the primary motivation of sharing/citing code is giving credit, where does Open Science fit? (e.g. Is one expected to ever cite individual scripts?; Can you cite software that doesn&#39;t have a &quot;title&quot;?; How do you share and point people to code that is meant for individual use? )
      1. Without clarifying this point in particular it is easy for people to become fixed on reproducibility issues (i.e. &quot;Perfect becomes the enemy of the good.&quot;)
   1. What are publishers supposed to do to educate referees?
   1. To what degree can automation support referees? (e.g. What can be done to flag papers that should have software citations?)

**Tools and Other Resources**

Throughout the splinter meeting, attendees also took time to brainstorm about possible tools that could support software citation implementation. Ideas for tools were diverse, but primarily focused on how automated tools could be used to initiate human action by authors and reviewers. The motivation behind developing tools in this context was to find ways to make software citation straightforward and to make giving credit for research software as much a part of writing a paper as citing an article or data source. Tool ideas were not vetted for feasibility, nor was there any consideration of who should create or fund these types of tools.

Ideas for tools included (in no particular order):

- &quot;Figure Tags&quot; - A way to automatically embed a software citation in figures and/or generate the current preferred software citation when the figure is generated (e.g. figures created using corner.py).
- &quot;Flag for review&quot; - Upon submission, a script could cross reference an article&#39;s text against a list of keywords or phrases that would indicate that a software citation is expected and trigger an alert for the reviewer.
- &quot;Look up service for preferred citations&quot; - Could cross-reference known sources of preferred citations and GitHub for CITATION.md files.
- Wizard to help code authors create CITATION.md files and/or CodeMeta.json files.

Splinter meeting attendees also pointed out a number of other resources that would be useful that were not geared toward automating publication processes. These included:

- Clear, brief, best practice guidelines for software citation addressing the spectrum of research software including example citations.
  - These could be general enough to be helpful for reviewers and authors and answer many of the above noted questions.
  - These guidelines would need to refer out directly to relevant publisher guidelines or be augmented by publishers as needed.
    - Could act as a template for publishers who do not currently have guidelines in place for software citation.
    - Could be used to recommend changes to current citation style guides and reference management tools.
  - Guidelines could include recommended practices that would support software reuse and give general direction to resources on software licensing.
- LaTeX templates that include links to software citation guidelines for specific publishers.

The splinter meeting attendees also brought up resources that are not specific to software citation implementation in Astronomy, but do touch on issues that impact the ability for academics to make a career writing software, which is fundamentally why giving credit for software is so essential. These included a lack of designated funding mechanisms/opportunities to support software development in astronomy. Attendees also highlighted their perception that funders do not require or fund software &quot;preservation&quot; and archiving in the same way that they may require for the preservation of data. It should be noted though that these perceptions may stem from limited awareness about existing policies from funders like the NSF, which does require software management in the same way it requires data management as it is considered to be a type of data.

**Editorial Policies**

Discussions during the splinter meeting often moved toward publisher editorial policies and how the astronomy community could influence them. Although it was noted repeatedly that the AAS has reasonable guidelines for publishing software papers and citing software, many other journals do not and might inadvertently create disincentives for citing software by limiting the number of citations authors can include in their papers. Moreover, meeting attendees lamented the limited attention that referees tend to give to software citations as they pertain to software version and use of preferred citations. Some attendees pointed out instances where articles that cited a software paper, or version of software, which predated their contributions would sometimes include them in the acknowledgement section and sometimes not. Editorial policies may not give specific enough guidance to publishing staff or assume that best practices are obvious. Increased dialog about editorial policies is needed between members of the astronomy community who are knowledgeable about software citation issues and journal editors who can influence policies for their respective journals.

## Limitations

The information presented in this document was gathered by using an unsystematic and unstructured approach and will miss aspects of the conversations had during the AAS splinter meeting. Aside from this reality though, there are other important limitations to highlight from this process:

The group selected to discuss barriers to implementing the FORCE11 Principles at the splinter meeting were people already involved in conversations about software citation in astronomy. They therefore likely do not represent the perspectives of the broader community who may have much more limited awareness about these issues. Anecdotes made up the majority of examples given during conversations and those examples may be outliers despite efforts to focus on issues that impact the community more holistically.

Another issue that will impact any next steps recommended within this document is the fact that no &quot;solutions&quot; will be comprehensive, seeing as the entire premise of responding to community needs sets up an inverse problem wherein we are attempting to determine causes based on a limited set of observations. This fact should not prevent steps from being taken. Scholarly communication ecosystems are multifaceted and &quot;solutions&quot; will be iterative.

Finally, this document did not focus on intellectual property issues surrounding software and software citation. Discussions during the AAS splinter meeting only peripherally touched on intellectual property, licensing, and software reuse.

## Next Steps

It would be advantageous to develop and promote brief guidelines to inform software authors in astronomy of what they can do to help ensure they are given credit for their work within the current scholarly communication landscape. These guidelines could point out simple steps to make their code more citable<sup>[9](https://guides.github.com/activities/citable-code/)</sup> and clarify some of the confusion about author expectations. The guidelines could also explain common methods for publishing software and address citation issues for each case. The guidelines could then be iteratively updated as questions posed by the splinter meeting attendees are addressed by the community. A separate set of short guidelines could be created on how to cite software and where to look for citations. In order for any of these guidelines to be impactful, they would need to include real examples and be promoted by institutions and individuals in as many settings as possible. Any guidelines created for the community would be a foundation on which an awareness campaign could be built, serving as a focal point for future debate and discussion.

In addition to concrete guidelines specific to astronomy, it would be valuable to develop a survey of publisher&#39;s policies and editorial practices that impact software citation in the field. A survey of this sort could then be used to frame conversations with different publishers and indexers about which tools would be most helpful in enabling implementation of the FORCE11 Principles and inform updates to guidelines. The survey would also give publishers and stakeholders data that could support changes to editorial practices.

Moreover, it would be useful to design a study on self-citation practices in astronomy in order to better understand how software authors currently share their own work with the broader scientific community. A study of this kind could act as a standard for comparison to better understand how citation practices change over time.

## Future Discussion Needed

Future conversations about software in astronomy are needed to address issues surrounding intellectual property, licensing, and copyright in particular. Research software preservation and resources to support preservation should also be discussed further in the context of software reuse.

# Appendix A

_The FORCE11 Software Citation Principles_

[https://doi.org/10.7717/peerj-cs.86](https://doi.org/10.7717/peerj-cs.86)

1. Importance: **Software should be considered a legitimate and citable product of research**. Software citations should be accorded the same importance in the scholarly record as citations of other research products, such as publications and data; they should be included in the metadata of the citing work, for example in the reference list of a journal article, and should not be omitted or separated. Software should be cited on the same basis as any other research product such as a paper or a book, that is, authors should cite the appropriate set of software products just as they cite the appropriate set of papers.
2. Credit and attribution: Software citations should facilitate giving scholarly **credit and normative, legal attribution to all contributors to the software** , recognizing that a single style or mechanism of attribution may not be applicable to all software.
3. Unique identification: A software citation should include a **method for identification that is machine actionable, globally unique, interoperable, and recognized** by at least a community of the corresponding domain experts, and preferably by general public researchers.
4. Persistence: **Unique identifiers and metadata** describing the software and its disposition should persist—even beyond the lifespan of the software they describe.
5. Accessibility: Software citations should facilitate **access to the software itself and to its associated metadata** , documentation, data, and other materials necessary for both humans and machines to make informed use of the referenced software.
6. Specificity: Software citations should facilitate **identification of, and access to, the specific version of software** that was used. Software identification should be as specific as necessary, such as using version numbers, revision numbers, or variants such as platforms.

Note: Bolding is not part of the formatting in the original publication of the principles.

# Appendix B

_Discussion Prompts_

Given the Software Citation Principles as a Goal:

- What are the most substantial barriers you experience when citing software?

| Perspective | Social Barriers | Technical Barriers | Policy-Related Barriers (publisher or otherwise) | Other |
| --- | --- | --- | --- | --- |
| Barriers for Developers |   |   |   |   |
| Barriers for Authors |   |   |   |   |

- What resources have you used to help you to cite software? (e.g. use cases, blogs, people, reference management tools, etc.)
- What resources are still needed in astronomy?
- What specific tools would be helpful when authoring papers and writing new codes? (e.g. LaTeX macros, CITATION file template on GitHub, etc.)
- What do you think would most impactful in raising awareness about software citation issues in astronomy?

# References

1. Katz, D. S. (2017). Software Citation: A Solution with a Problem. Retrieved from https://www.slideshare.net/danielskatz/software-citation/danielskatz/software-citation
2. Smith, A. (2018). _Spectrum of Research Software_. Retrieved from https://stsci.app.box.com/s/ooamf3ds1fxcqq7nnhgpnbjgi0sra031
3. Muench, A. (2018). Implementations and provocations from the asclepias project. Retrieved from https://drive.google.com/file/d/1LB1arge6mMSHz1Lgxu6wn8Nr-Rb1LYNw/view?usp=embed\_facebook
4. Smith, A. M., Katz, D. S., &amp; Niemeyer, K. E. (2016). Software citation principles. _PeerJ Computer Science_, _2_, e86. https://doi.org/10.7717/peerj-cs.86
5. Druskat, S., Bast, R., Chue Hong, N., Konovalov, K., &amp; Rowley, A. (2017). A standard format for CITATION files. _Software Sustainability Institute: Software and Research Blog_. Retrieved from https://www.software.ac.uk/index.php/blog/2017-12-12-standard-format-citation-files
6. Katz, D. S., &amp; Smith, A. M. (2014). Implementing Transitive Credit with JSON-LD. _ArXiv:1407.5117 [Cs]_. Retrieved from http://arxiv.org/abs/1407.5117
7. Citations, software. (2017). Retrieved from http://www.metrics-toolkit.org/citations-software/
8. Chue Hong, N., Druskat, S., &amp; Slaughter, P. (2018). _codemeta: Minimal metadata schemas for science software and code, in JSON-LD_. CodeMeta. Retrieved from https://github.com/codemeta/codemeta/blob/master/codemeta.json
9. Smith, A. (n.d.). Making Your Code Citable · GitHub Guides. Retrieved from https://guides.github.com/activities/citable-code/
