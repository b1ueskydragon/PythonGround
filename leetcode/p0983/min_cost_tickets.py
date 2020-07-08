class Solution:
    def mincostTickets(self, days: [int], costs: [int]) -> int:
        travel_days = [-1] * 366
        for day in days:
            travel_days[day] = day
        payments = [0] * 366
        once, week, month = costs[0], costs[1], costs[2]
        prev_day = 0
        for i, day in enumerate(travel_days):
            if day == -1:
                payments[i] = payments[prev_day]  # no trip day == total payment is same as prev day
                continue
            acc_week = week
            if day >= 7:
                acc_week = (float('inf'), payments[day - 7] + week)[day >= 7]
            acc_month = month
            if day >= 30:
                acc_month = (float('inf'), payments[day - 30] + month)[day >= 30]
            payments[day] = min(payments[prev_day] + once, acc_week, acc_month)
            prev_day = day

        # print(payments)
        return payments[days[-1]]
