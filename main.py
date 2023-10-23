def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    mnum = int(input("Enter number of males: "))
    fnum = int(input("Enter number of females: "))

    total = mnum + fnum
    m_perc = mnum / total * 100
    f_perc = fnum / total * 100
    print(f'The Percentage of the male student is {m_perc:.2f}')
    print(f'The Percentage of the female student is {f_perc:.2f}')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
