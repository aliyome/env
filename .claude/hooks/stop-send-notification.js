#! /usr/bin/env node

import { execFileSync } from "node:child_process";
import { readFileSync } from "node:fs";
import path from "node:path";
import os from "node:os";

try {
    const input = JSON.parse(readFileSync(process.stdin.fd, 'utf8'));
    if (!input.transcript_path) {
        process.exit(0);
    }

    const homeDir = os.homedir();
    let transcriptPath = input.transcript_path;

    if (transcriptPath.startsWith('~/')) {
        transcriptPath = path.join(homeDir, transcriptPath.slice(2));
    }

    const allowedBase = path.join(homeDir, '.claude', 'projects');
    const resolvedPath = path.resolve(transcriptPath);

    if (!resolvedPath.startsWith(allowedBase)) {
        process.exit(1);
    }

    const lines = readFileSync(resolvedPath, "utf-8").split("\n").filter(line => line.trim());
    if (lines.length === 0) {
        process.exit(0);
    }

    const lastLine = lines[lines.length - 1];
    const transcript = JSON.parse(lastLine);
    const lastMessageContent = transcript?.message?.content?.[0]?.text;

    if (lastMessageContent) {
        const script = `
          try
            set notificationTitle to system attribute "CLAUDE_NOTIFICATION_TITLE"
            set notificationMessage to system attribute "CLAUDE_NOTIFICATION_MESSAGE"
            display notification notificationMessage with title notificationTitle
          end try
        `;
        execFileSync('osascript', ['-e', script], {
            env: {
                ...process.env,
                CLAUDE_NOTIFICATION_TITLE: "Claude Code",
                CLAUDE_NOTIFICATION_MESSAGE: lastMessageContent,
            },
            stdio: 'ignore'
        });
    }
} catch {
    process.exit(1);
}