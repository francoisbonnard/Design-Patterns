[course AWS](https://www.youtube.com/watch?v=XZbvQWkpJTI)

![Networking services you should know](image-1.png)


![fg.com on AWS](image-2.png)

## Let's start


![VPC comes with local router](image-3.png)
![Alt text](image-15.png)

![Public Subnets inside](image-4.png)

![10.10.0.0/24](image-5.png)

![10.10.1.0/24](image-6.png)

![iNTERNET GATEWAY](image-7.png)

![Route Table for the subnet](image-8.png)

![Private Subnet](image-9.png)

![route table for private subnet](image-10.png)

![More private subnet](image-11.png)

![Load Balancer](image-12.png)

![Load balancer detail](image-17.png)

![EC2 Web/app server](image-13.png)

![Database](image-14.png)

![Database replication](image-16.png)

![adding NAT](image-18.png)

![private subnet route table for NATs](image-19.png)

![Final result](image-31.png)

![From Cegos Lab2](image-30.png)

![Hybrid connectivity](image-20.png)

Secure but not reliable

Better solution with direct connect partner (or on your own)

![direct connect](image-21.png)

![client VPN endpoint for remote workers](image-22.png)

need openVPN server client for the remote workers

![Multiple VPC](image-23.png)

VPC peering is non transitive : needs 1 to 1 connection

To remedy that :

![transit gateway](image-24.png)

Advanced topics of VPC : vpc endpoint services

![access S3 from EC2](image-25.png)

could be a problem (if NAT goes down or for secured reasons)

![VPC endpoint gateway](image-26.png)

VPC endpoint gateway to reach S3 or DynamoDB

if we want to use more services : 

![VPC endpoint services](image-27.png)

So it creates ENI Elastic Network interface inside the subnet

![ENI](image-28.png)

If we subscribe to SAAS services and if all VPCs are inside AWS : we can use Private Link

![private link](image-29.png)


