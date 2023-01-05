#!/usr/bin/python3
#!/usr/bin/python3

def main():
    import hidden_4
    names = dir(hidden_4)
    for name in names:
        if name.startswith("__"):
            continue
        print(name)


if __name__ == "__main__":
    main()
