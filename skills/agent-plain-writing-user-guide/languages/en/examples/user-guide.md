# English examples: user guide

## Replacing jargon

| Jargon | Say this to the user |
|---|---|
| cache | saved data |
| token | sign-in code |
| API key | connection code |
| sync | updates on all your devices automatically |
| authenticate | sign in |
| two-factor authentication | an extra check with a code sent to your phone |
| session expired | the app asks you to sign in again |
| backup | a saved copy |
| restore | get it back from the saved copy |
| configure | set up, change the settings |
| firmware | the software inside the device |
| server | (leave out if not needed) |
| log | activity history |

If a term **appears on the screen** (for example a button labeled "Token"), use that exact word and explain it once.

## Bad → good pairs

### 1. A step with many actions

**Bad:** Please navigate to the settings area, then locate the account section and proceed to change your password by entering your old and new passwords.
**Good:**
1. Click **Settings**.
2. Select **Account**.
3. Click **Change password**.
4. Enter your old password, then your new password.
5. Click **Save**. You will see "Password changed".

### 2. Mechanism → result

**Bad:** The app uses a background synchronization mechanism to automatically update data between devices through a cloud server.
**Good:** Edit on your phone. Your computer updates too. You don't need to do anything.

### 3. Jargon

**Bad:** If your token expires, you will need to re-authenticate.
**Good:** If the app says your sign-in has expired, sign in again.

### 4. Warning

**Bad:** Please note that deleting data may, in some circumstances, result in it being unrecoverable.
**Good:** **Warning:** Deleted data cannot be restored.

### 5. Handling errors

**Bad:** In the event of an error, please verify your network connection or contact technical support for assistance.
**Good:**

| You see | What to do |
|---|---|
| "Can't connect" | Check your Wi-Fi, then try again. |
| Still fails after retrying | Take a screenshot and send it to [support address]. |

### 6. Describing a feature with adjectives

**Bad:** The reporting feature offers a wide range of options that enable users to comprehensively analyze their data.
**Good:** Use **Reports** to see how much you sold this month.

### 7. Dumping the mechanism (a common fault)

**Bad:** When you click Send, the request is added to a processing queue. A background process picks it up, validates the data, and writes it to the database. You are then notified of the result by email.
**Good:** Click **Send**. A few minutes later, you get an email with the result.
**Rule:** Ask "why does the user need to know this?" If there is no reason, delete it.

### 8. Wrong button name

**Bad:** Press the confirm button to save your changes.
**Good:** Click **Save**.

### 9. Prerequisite

**Bad:** Before proceeding, you must ensure that the necessary permissions have been granted to your account.
**Good:** You need to be an **Administrator**. If you don't see the **Add** button, ask an administrator for access.

### 10. Goal

**Bad:** This guide aims to provide users with the information necessary to utilize the report export functionality.
**Good:** This guide shows you how to export a report to an Excel file.

## Complete sample guide

```markdown
# Change your password

Use this when you forgot your password or want a new one.

## Before you start
- You are signed in.
- You remember your old password.

## Steps
1. Click **Settings**.
2. Select **Account**.
3. Click **Change password**.
4. Enter your old password, then enter your new password twice.
5. Click **Save**. You will see "Password changed".

## If something goes wrong

| You see | What to do |
|---|---|
| "Old password is incorrect" | Enter it again. If you forgot it, click **Forgot password** on the sign-in screen. |
| "Password too short" | Use at least 8 characters. |
```

## Your own samples

<!-- Paste a guide you wrote well, and AI sentences that explain too much with your short version. -->
