nums = [int(input()) for _ in range(10)]
reminders = []
for i in nums :
    if i%42 not in reminders :
        reminders.append(i%42)

print(len(reminders))
