# Reliance-stock-Anlaysis


Tools used: Pandas,streamlit,numpy,sklearn

The hidden Markov model (HMM) is a signal prediction model which has been used to predict economic regimes and stock prices. This project intends to achieve the goal of applying machine learning algrithms into stock market. The long short term memory model (LSTM) ensures that the previous information can continue to propagate backwards without disappearing as the hidden layer continuously superimposes the input sequence under the new time state.

# Process
Using data from 1996-2020 in Reliance share stock market, including daily price and trade volume and over 200 types of feature, we divided them into 8 types of features and make 8 HMMs. Then combined them together to predict ups and downs of stock price the next day. During which, we used GMM and XGBoost to fit the emission matrix B of continuous HMMs and used LSTM to find a better connection of X and Y. Moreover, an useful method of labeling called the reiple barrier method is well used to find relationship between hidden states and the trends of stock price.

# Close vs moving average of first 100 records
![Screenshot_7](https://user-images.githubusercontent.com/106678356/218077319-d9648e89-943c-428d-b853-938d3f325693.png)

# Close vs moving average of first 200 records
![Screenshot_8](https://user-images.githubusercontent.com/106678356/218077569-c29a0eb1-fc8a-4c4c-ae54-73e84d4134a3.png)
