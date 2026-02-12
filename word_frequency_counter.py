def main():   
    user_input=input("Enter the sentence: ")
    words=user_input.lower().split()
    words_count={}
    for word in words:
        if word in words_count:
            words_count[word] +=1
        else:
            words_count[word]=1
    for words, count in words_count.items():
        print(f"{words}, {count}")

if __name__=="__main__":
    main()