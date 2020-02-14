# Notifications that AWS Config Sends to an Amazon SNS topic<a name="notifications-for-AWS-Config"></a>

You can configure AWS Config to stream configuration changes and notifications to an Amazon SNS topic\. For example, when a resource is updated, you can get a notification sent to your email, so that you can view the changes\. You can also be notified when AWS Config evaluates your custom or managed rules against your resources\. 

AWS Config sends notifications for the following events:
+ Configuration item change for a resource\.
+ Configuration history for a resource was delivered for your account\.
+ Configuration snapshot for recorded resources was started and delivered for your account\.
+ Compliance state of your resources and whether they are compliant with your rules\.
+ Evaluation started for a rule against your resources\. 
+ AWS Config failed to deliver the notification to your account\. 

**Topics**
+ [Example Configuration Item Change Notifications](example-sns-notification.md)
+ [Example Configuration History Delivery Notification](example-configuration-history-notification.md)
+ [Example Configuration Snapshot Delivery Started Notification](example-configuration-snapshot-notification-started.md)
+ [Example Configuration Snapshot Delivery Notification](example-configuration-snapshot-notification.md)
+ [Example Compliance Change Notification](example-config-rule-compliance-notification.md)
+ [Example Rules Evaluation Started Notification](config-rules-evaluation-started.md)
+ [Example Oversized Configuration Item Change Notification](oversized-notification-example.md)
+ [Example Delivery Failed Notification](notification-delivery-failed.md)