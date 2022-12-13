# IDS 706 Group Project

### Group Memeber: Ruixin Lou, Yuyou Wu, Lei Duan, Yunan Liu

## This is an api application based on fast-api.

## The application was built to connect to google cloud platform database, and perform data processing to the StackOverflow dataset, which merged the posts id dataset and the posts rating dataset, and sorted the merged dataset in a descending order. The output is the top five posts that have the highest rating.

## The top five posts information can be shown through /topfive command in the url of fast api application.
![Alt text](/workspaces/Yunan_Group_Proj/topfive.png)


## The application is pushed to AWS ECR and AWS app runner, and the aws app runner's auto deploy function is turn on, which allows the app runner to update automatically when new (updated) docker image is pushed to AWS ECR.
