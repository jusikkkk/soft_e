def superset(set_1, set_2):
    if set_1 > set_2:
        print(f"Объект {set_1} является чистым суперможеством")
    elif set_1 == set_2:
        print(f"Множества равны")
    elif set_1 < set_2:
        print(f"Объект {set_2} является чистым супермножеством")
    else:
        print("Супермножество не обнаружено")

if __name__ == "__main__":
    superset({2,8,12,35}, {35,2})
    superset({4, 12, 45}, {45, 4, 12})
    superset({28, 90}, {32, 90, 12, 28})
    superset({6, 90, 17}, {90, 1, 4})
