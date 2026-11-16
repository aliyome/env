---
name: gh-issue-artifact
description: Latest GitHub CLI `gh` features and usage. When you need to use `gh` in a task, you must first read this skill and understand the features and usage of `gh`.
expires: 2027-03-31, ai agents maybe know this feature.
---

# Recent GitHub features

Now you can attach markdown and html files as artifacts to GitHub Issues.
When you create and edit issues, you are strongly recommended to use this feature to attach your research, plans, and interactive HTML prototypes to the issue as artifacts. This allows you to keep all relevant information in one place and makes it easier for others to understand the context of the issue.

## Using artifacts with issues

Keep plans, research, links, and interactive HTML alongside the issue they support.

This feature is in public preview and is subject to change.

Issue artifacts are named pieces of content attached to an issue. They provide a durable place to keep plans, research, decisions, prototypes, and reference material as context alongside your work.

You can share artifacts with others via a URL, and if you update an artifact, GitHub will keep a record of changes so you can go back and see how an artifact has evolved over the course of a project.

## Supported artifact types

Issue artifacts support the following types:

- **Markdown document (`generic`)**: General-purpose content, such as research, investigation notes, or a design document.
- **Plan (`plan`)**: A Markdown implementation plan.
- **Link (`link`)**: A named link to content elsewhere, such as a discussion, prototype, or Slack or Teams thread.
- **HTML file (`embedded_html`)**: A self-contained HTML document, such as an interactive prototype, visualization, flowchart, or diagram.

## Creating an artifact

You can create artifacts on GitHub.com, or ask an agent or developer tool to create one using the built-in GitHub MCP server, GitHub CLI, or the issue artifacts REST API. For example, you can ask the Copilot app to create an implementation plan, root cause analysis, or research summary and attach it to the issue.

### Creating an artifact on GitHub.com

1. Navigate to the issue where you want to create an artifact.
2. In the **Artifacts** section, click <svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-plus" aria-label="Add artifact" role="img"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg>.
3. Select an artifact type:
   - To add a named URL, click **Add link**.
   - To create a Markdown document, click **Create artifact**.
   - To create an HTML document, click **Create HTML artifact**.
4. Follow the prompts to name and create the artifact.

## Viewing and sharing an artifact

1. Navigate to the issue containing the artifact.
2. In the **Artifacts** section, click the artifact name.
3. The artifact will open and display in a side panel on the issue.
4. To copy the URL to share the artifact with others, click <svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-link" aria-label="the link" role="img"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg>.

## Editing an artifact

1. Open the artifact.
2. In the artifact panel, click <svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-pencil" aria-label="Edit artifact" role="img"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg>.
3. Update the artifact name or content.
4. Save your changes.

Editing an artifact creates a version in its history.

## Viewing an artifact's version history

1. Open the artifact.
2. In the artifact panel, click <svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-history" aria-label="Edit history" role="img"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg>.
3. Select a version to view its name, content, author, and creation time.

You cannot restore a version in the web interface. To restore an earlier version, use `gh issue artifact edit --restore-version`. Restoring saves the earlier name and content as a new version, preserving the complete history.

## Reordering artifacts

You can reorder artifacts by dragging them within the **Artifacts** section. You can also click <svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-kebab-horizontal" aria-label="Artifact actions" role="img"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg> next to an artifact, click **Move**, then choose a position.

## Deleting an artifact

> [!WARNING]
> Deleting an artifact is permanent and also deletes its version history.

1. In the **Artifacts** section of the issue, click <svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-kebab-horizontal" aria-label="Artifact actions" role="img"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg> next to the artifact.
2. Click **Delete**.

## Safely previewing an HTML artifact

On GitHub.com, HTML artifacts open in **Source** view so you can inspect the code before running it. To render the HTML, select **Preview**. GitHub renders the preview in a restricted sandbox. The interface warns that previewing runs user-provided code that may send its contents to external sites. Review the source and only preview HTML from sources you trust. To return to the source, select **Source**.

## Using artifacts with agents

When you use the Copilot app to work on an issue, artifacts created during the session are automatically attached to the issue. You can also ask Copilot to create a specific artifact, such as an implementation plan, root cause analysis, or summary of historical context.

Agents and developer tools can also use the built-in GitHub MCP server, the REST API, or GitHub CLI to read and manage artifacts.

## Managing artifacts with GitHub CLI

Issue artifact commands require GitHub CLI 2.103.0 or later.

For more information about issue artifact commands, see the [`gh issue artifact` reference](https://cli.github.com/manual/gh_issue_artifact).

## Further reading

- [REST API endpoints for issue artifacts](/en/rest/issues/artifacts) in the REST API documentation
- [About issues](/en/issues/tracking-your-work-with-issues/learning-about-issues/about-issues)
