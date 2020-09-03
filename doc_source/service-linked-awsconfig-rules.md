# Service\-Linked AWS Config Rules<a name="service-linked-awsconfig-rules"></a>

A service\-linked AWS Config rule is a unique type of managed config rule that supports other AWS services to create AWS Config rules in your account\. The service\-linked AWS Config rules are predefined to include all the permissions required to call other AWS services on your behalf\. These rules are similar to standards that an AWS service recommends in your AWS account for compliance verification\. 

These service\-linked AWS Config rules are owned by AWS service teams\. The AWS service team creates these rules in your AWS account\. You have read\-only access to these rules\. You cannot edit or delete these rules if you are subscribed to AWS service that these rules are linked to\.

In the AWS Config console, the service\-linked AWS Config rules are visible in the **Rules** page\. The edit button is greyed in the console thereby restricting you to edit the rule\. You can view details of the rule by choosing the rule\. On the rule details page, you can view the name of the service that created the rule\. The **Edit** and **Delete results** is greyed thereby restricting you to edit and delete results of the rule\. To edit or delete the rule, contact the AWS service that created the rule\. 

While using the AWS Command Line Interface, the `PutConfigRule`, `DeleteConfigRule`, and `DeleteEvaluationResults` APIs return access denied with the following error message:

`INSUFFICIENT_SLCR_PERMISSIONS = "An AWS service owns ServiceLinkedConfigRule. You do not have permissions to take action on this rule." ` 

**Topics**
+ [Using Service\-Linked Roles for AWS Config](using-service-linked-roles.md)