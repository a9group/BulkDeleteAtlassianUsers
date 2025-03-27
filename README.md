Atlassian currently lacks a native feature for bulk user deletion in Jira Cloud. While there is an open feature request for this capability, Atlassian has indicated that their immediate focus is on developing APIs to assist customers in managing users programmatically. Once these APIs are delivered, they will reassess the priority of integrating bulk actions into the user interface. ​

In the interim, administrators seeking to delete multiple users must rely on alternative methods, such as using REST APIs in conjunction with tools like Postman. Atlassian provides guidance on this approach, detailing how to configure Postman to process user deletions via REST API calls. ​

Given this landscape, we've developed a Python script that leverages the requests library to facilitate bulk user deletion in Jira Cloud. This tool enables administrators to automate the deletion process by reading user information from a CSV file and making the necessary API calls to remove users from the system. By using this script, organizations can efficiently manage user accounts without waiting for native bulk deletion features to be implemented.​

