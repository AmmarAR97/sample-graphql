# mikelegal

Build an Email Campaign Manager that can do the following:

1. Add Subscribers ('email', 'first_name')
    - An endpoint to unsubscribe users.
2. Mark unsubscribed users as "inactive”.
3. Use Django admin to add new records to each table. (*If you are not using Django for the task, expose an endpoint HTML page to add records into those tables with proper permissions*)
4. Write a function to send daily Campaigns using SMTP ( you can create a Mailgun sandbox account)
    - Each Campaign has 'Subject', 'preview_text', 'article_url', 'html_content', 'plain_text_content', 'published_date'.
    - Campaign email must be rendered with the above information from a base template.
5. Optimize the sending time by using pub-sub with multiple threads dispatching emails in parallel.
