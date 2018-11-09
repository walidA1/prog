while True:
    aantal = input("Aantal: ")
    try:
        aantal = int(aantal)
        kosten_pp = 4356/aantal
        assert aantal > 0
    except ValueError:
        print("Gebruik cijfers voor het invoeren van het aantal!")
        continue
    except ZeroDivisionError:
        print("Delen door nul kan niet!")
        continue
    except AssertionError:
        print("Negatieve getallen zijn niet toegestaan!")
        continue
    except:
        print("Onjuiste invoer!")
        continue
    else:
        print("het te betalen bedrag per persoon is €{:.2f}".format(kosten_pp))
        break
