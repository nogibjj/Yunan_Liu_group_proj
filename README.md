# IDS 706 Group Project

### Group Memeber: Ruixin Lou, Yuyou Wu, Lei Duan, Yunan Liu

## This is an api application based on fast-api.

## Here is how the welcome page of the api look like
![Alt text](/readme_source/welcome.png)

## The application was built to connect to google cloud platform database, and perform data processing to the StackOverflow dataset, which merged the posts id dataset and the posts rating dataset, and sorted the merged dataset in a descending order. The output is the top five posts that have the highest rating.

## The top five posts information can be shown through /topfive command in the url of fast api application.
![Alt text](/readme_source/topfive.png)

## Calculator funciton

## Through type in the numbers and operation symbol in the url, the api will return the result in the REST interface. It currently only allows simple calculations(addition, substraction, multiplication and division). 
### * For the division operation, the user will need to use 'd' instead of '/' as operation symbol.

![Alt text](/readme_source/substract.png)

## The api will also handle some basic errors, such as divisor being zero, and invalid operational symbol
![Alt text](/readme_source/error.png)

## The application is pushed to AWS ECR and AWS app runner, and the aws app runner's auto deploy function is turn on, which allows the app runner to update automatically when new (updated) docker image is pushed to AWS ECR.
![Alt text](/readme_source/apprunner.png)
![Alt text](/readme_source/apppush.png)