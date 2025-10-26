# Agile Basics

# QUESTIONS

How do you organize a team of engineers toward the singular goal of delivering frequent, high-value changes to an application?  
This is a question that has been asked for decades, and while today we have a strong set of answers, that was not always the case.

---

## What is Agile?

Agile is a way of working that focuses on delivering small, usable pieces of a project quickly and iteratively.  
It values **flexibility**, **customer feedback**, and **continuous improvement** over rigid upfront planning.

Agile is not a set of tools or strict rules — it is a mindset focused on **responding to reality** rather than trying to predict it perfectly.


---

## Quick History of Agile

In 2001, 17 software developers gathered at a ski resort in Snowbird, Utah.  
They came from different backgrounds but shared a frustration with traditional, heavyweight software development processes like Waterfall.

Together, they drafted the **Agile Manifesto**, a short and powerful statement about better ways to build software.  
Since then, Agile has evolved into the dominant philosophy for modern software engineering — and beyond.

---

## Waterfall vs Agile

| Waterfall | Agile |
|:---|:---|
| Plan everything up front | Plan in small pieces |
| Deliver all at once at the end | Deliver small parts frequently |
| Changes are expensive and hard | Changes are expected and embraced |

> Waterfall Scenario:
They spend 4 months designing every single page, writing detailed requirements, and planning features like the shopping cart, user accounts, payment processing, and order tracking, before writing a single line of code.
Only after all designs and documents are "perfect" do developers start coding.
Six months later, when they finally launch the site, they discover customers find the checkout process confusing,
Mobile users say the site loads too slowly.
Many of the planned features (like a complex loyalty points system) weren't even important to early users.
Now it's expensive and painful to fix, because the site was built based on assumptions made almost a year ago.

> Agile Scenario
Same company, new mindset.
The team agrees on a minimal first goal: "Get users to browse products and check out smoothly on desktop and mobile."
They design and launch a basic homepage, product pages, and a simple checkout within the first 2-week sprint.
They immediately get feedback: customers love browsing, but complain the checkout takes too long.
In the next sprint, the team streamlines checkout to 3 clicks.
Every 2 weeks, they improve based on real customer data, adding real value sooner, and avoiding building features nobody cares about.

Key lessons from the example:
- Waterfall risks building something undisirable
- Agile tends to build something messy first, and refine it based on early feedback
- Getting early feedback is ESSENTIAL

---

## Agile Manifesto - Core Values

**Individuals and interactions over processes and tools**
- Focus on people talking to each other directly, solving real problems quickly, instead of relying heavily on formal procedures or documentation.

**Working software over comprehensive documentation**
- Prioritize building a working login page over writing a 100-page specification document about how the login page should eventually work.

**Customer collaboration over contract negotiation**
- Instead of arguing about "what the contract says" when a customer's needs change, Agile teams talk to customers and adjust goals based on their evolving priorities.

**Responding to change over following a plan**
- Instead of stubbornly sticking to a 6-month-old roadmap that no longer fits reality, Agile teams welcome changes that better meet user needs.

**Core Message:**  
Agile prioritizes **real outcomes**, **real users**, and **the ability to adapt** over strict procedures.

It is not about being unstructured or chaotic — it's about having the **right amount of structure to stay flexible**.

---

## Scrum Overview (Agile Framework)

**Roles:**
- **Product Owner**: Owns the vision, defines priorities, and acts as the voice of the customer.
> Communicates directly with stakeholders to get feedback and direction, translates these needs to the technical team.

- **Scrum Master/Agile Coach**: Coaches the team on Agile practices and removes obstacles.
> Maintains and enforces the systems and procedures around agile principles and ceremonies for their teams.

- **Development Team**: Builds and delivers usable product increments each sprint.
> You (most likely)

**Terms:**
- **Sprint**: A given session of work usually 2 weeks where the team focuses on specific goals.
- **Product Backlog**: Ordered list of everything the product might need for the rest of it's forseeable future.
- **Sprint Backlog**: Selected work for the current sprint.
- **Increment**: The collection of completed work at the end of a sprint — always in a usable state.

**Events:**
- **Sprint Planning**: Sprint Planning: A collaborative meeting where the team and Product Owner decide what work will be accomplished during the sprint. The team asks questions, estimates work effort, and commits to a set of goals.
- **Daily Scrum (Standup)**:  
  A 15-minute team meeting for **coordination**, not status reporting — focused on what’s being worked on and any obstacles. Team members typically answer three questions: What did I do yesterday? What will I do today? Are there any obstacles?
- **Sprint Review**: At the end of the sprint, the team presents the completed increment to stakeholders for feedback. This is an opportunity to inspect and adapt the product direction.
- **Sprint Retrospective**: A reflection meeting held after the Sprint Review, focused on how the team worked together. The team discusses successes, challenges, and specific actions to improve future sprints. Typically there are specific questions, What went well this sprint, what did not go well, what needs to change?

---

## Benefits and Common Challenges

### Benefits:
- Faster delivery of usable software to customers.
- Early detection of risks and misunderstandings.
- Improved collaboration across developers, designers, product managers, and clients.
- Greater team ownership and morale when done correctly.

### Common Challenges:
- **Scope Creep**: Goals expanding mid-sprint without discipline.
- **Resistance**: Some teams or managers are uncomfortable with less predictability.
- **Misunderstanding Agile**: Agile is not \"just do whatever\" — it requires structure and intentional iteration.

---

## Key Agile Concepts

| Concept | Meaning | Scenario |
|:---|:---|:---|
| **Iteration** | Short, repeatable cycles of work. | Deliver a working login page every two weeks. |
| **Increment** | Usable part of the product. | A basic homepage, not a half-built homepage. |
| **Backlog** | Dynamic prioritized task list. | \"Add profile picture upload\" as a backlog item. |
| **Sprint** | Fixed work period (e.g., 2 weeks). | Team focuses on a few clear goals without new distractions. |
| **Retrospective** | Reflection meeting to improve. | After a sprint, team discusses what to improve next time. |
| **Scrum** | Common Agile framework. | Morning standups, sprint reviews, and retrospectives. |

---

## Quick Recap

- Agile focuses on **flexibility**, **incremental delivery**, and **continuous user feedback**.
- Scrum provides a structure for applying Agile principles effectively.
- Agile is about being **structured enough to adapt**, not about avoiding structure.

Agile is used not just in software, but increasingly in marketing, operations, education, and other fields where rapid change and feedback are critical.

---

# Agile Activity: Build Your First Sprint Plan with Trello

Welcome to your first Agile project simulation!  
Your team will create a **Sprint Plan** for a brand-new clone of a popular app.

---

## Instructions

### 1. Form Your Team
- Work with the people in your row (3–5 members per team is ideal).

### 2. Choose Your App to Clone
Pick one app to rebuild from scratch:
- A **simple Spotify** (music playlist app)
- A **basic Trello** (task board app)
- A **mini Twitter** (microblogging app)

**Important:** Start with a *very basic* version — your goal is a **Minimum Viable Product (MVP)**, not a full-scale rebuild.

---

## Trello Setup

1. Go to [https://trello.com](https://trello.com) and create a free account if you don’t have one.
2. Create a new Board. Name it after your project (e.g., "Team Echo - Mini Spotify").
3. Create these 3 Lists:
   - **Product Backlog** (all ideas and features you might want)
   - **Sprint Backlog** (features you are committing to this sprint)
   - **Done** (completed tasks)

---

## Sprint Planning

Your first Sprint is **5 days** long (imagine one full week of work).

### Steps:

1. **Brainstorm 5–8 User Stories**
   - Use this format:  
     > "As a (type of user), I want (goal) so that (reason)."
   
   Example user stories:
   - "As a listener, I want to create playlists so that I can organize my favorite songs."
   - "As a user, I want to post tweets so that I can share my thoughts instantly."

2. **Prioritize and Select 3–5 User Stories for This Sprint**
   - Pick the most important and realistic features for an MVP.
   
3. **Estimate Effort for Each Story**
   Use these estimates:
   
   | Effort Size | Definition |
   |:------------|:-----------|
   | Small | Less than 1 day of work (1–2 simple tasks) |
   | Medium | 1–3 days of work (multiple steps or a more complex feature) |
   | Large | 4–5 days of work (big features that might need breaking down) |

4. **Assign Tasks**
   - Break user stories into tasks if necessary.
   - Assign one or more team members to each task.

5. **Set Deadlines**
   - Make sure all selected stories have deadlines *within the 5-day sprint.*

6. **Organize the Board**
   - Product Backlog: All brainstormed user stories.
   - Sprint Backlog: Stories selected for this sprint.
   - Done: Stories or tasks you complete.

---

## Submission

- When you finish your board setup, **submit the link to your Trello board**.
- Title your board with your Team Name and Project (e.g., "Team Echo - Mini Spotify").

---

## Reflection (Required)

After submitting your board, each team must answer the following:

1. What was hardest about prioritizing your user stories?
2. How did your team estimate effort — was it easy or challenging?
3. On a scale of 0–5, how confident are you in your sprint plan, and why?

---

## Key Reminders

- **Focus on MVP**: Build something *small and real* — not every feature under the sun.
- **Agile is not about the tool**: Trello helps you *visualize work*, but real Agile is about *communication, flexibility, and focus*.
- **Aim for done, not perfect**: Finished small features are better than half-built big ones.

---

## Goal of this Activity

- Practice Agile-style sprint planning.
- Understand how to break ideas into manageable, achievable tasks.
- Experience how real teams prioritize, estimate, and collaborate under time pressure.
- Learn how to use a visual board to organize a project.

---
