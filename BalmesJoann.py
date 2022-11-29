if __name__ == "__main__":
    
    def division(first_num,second_num):
        try:
            quotient = first_num/second_num
            print(f"{first_num}/{second_num}= {quotient}")
        except ZeroDivisionError as e:
            print("Exception occured!:", e)
        except Exception as e:
            print("Exception occured!:", e)
            
    first_num = int(input("Enter First Number: "))
    second_num = int(input("Enter Second Number: "))
    division(first_num,second_num)