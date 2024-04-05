aws dynamodb put-item --table-name Student_Result --item '{"ID": {"N": "1001"}, "Name": {"S": "Kader"}, "Status": {"S": "Pass"}}'

aws dynamodb put-item --table-name Student_Result --item '{"ID": {"N": "1002"}, "Name": {"S": "Zakir"}, "Status": {"S": "Fail"}}'

aws dynamodb put-item --table-name Student_Result --item '{"ID": {"N": "1003"}, "Name": {"S": "Jakia"}, "Status": {"S": "Pass"}}'

aws dynamodb put-item --table-name Student_Result --item '{"ID": {"N": "1004"}, "Name": {"S": "Pervez"}, "Status": {"S": "Waiting"}}'