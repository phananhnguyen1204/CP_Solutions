from heapq import heappush, heappop
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buyBackLog = []
        sellBackLog = []
        for order in orders:
            price, amount, t = order
            #We are selling, looking for max buy
            if t == 1:
                while amount > 0 and buyBackLog:
                    buyPrice, buyAmount, buyType = buyBackLog[0]
                    buyPrice *= -1
                    if buyPrice >= price:
                        transactionAmount = min(amount, buyAmount)
                        amount -= transactionAmount
                        buyAmount -= transactionAmount
                        heappop(buyBackLog)
                        if buyAmount > 0:
                            heappush(buyBackLog, (-buyPrice, buyAmount, buyType))
                    else:
                        break

                #unsuccessful
                if amount > 0:
                    heappush(sellBackLog, (price, amount, t))
            # WE are buying, looking for min sell
            else:
                while amount > 0 and sellBackLog:
                    sellPrice, sellAmount, buyType = sellBackLog[0]
                    if sellPrice <= price:
                        transactionAmount = min(amount, sellAmount)
                        amount -= transactionAmount
                        sellAmount -= transactionAmount
                        heappop(sellBackLog)
                        if sellAmount > 0:
                            heappush(sellBackLog, (sellPrice, sellAmount, buyType))
                    else:
                        break


                #unsuccessful
                if amount > 0:
                    heappush(buyBackLog, (-price, amount, t))
        res = 0
        while sellBackLog:
            res += sellBackLog[0][1]
            heappop(sellBackLog)
        while buyBackLog:
            res += buyBackLog[0][1]
            heappop(buyBackLog)
        return res  % (10**9 + 7)