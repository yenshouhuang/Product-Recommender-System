# product-recommender-system

###In Python only

####Task:
- Use association rules (Arpiori Algorithm) to predict customer next-to-purchase preference

####Approach:

- We consider the 1374 customers who have at least 100 orders and use their transaction data to analyze. 
- We consider the top 97 orders as purchase history data for training and
consider the rest 3 orders will be considered as shopping cart data for testing.
- Examine if customer has purchased the items in the orders of testing data. If customer purchased the items beofre, use customer's personal purchase history data to train algorithm and predict next item. If customer didn't purchase the items beofre, use purchase history data from all users to train algorithm and predict next item.


####Resources:
- [Database: Instacart Market Basket Analysis] (https://www.kaggle.com/c/instacart-market-basket-analysis/data)
