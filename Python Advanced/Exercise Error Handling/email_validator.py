class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = ["com", "bg", "org", "net"]
while True:
    command = input()
    if command == "End":
        break

    if "@" not in command:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain = command.split("@")
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    get_domain = domain.split(".")
    if len(get_domain) > 1:
        if get_domain[1] not in valid_domains:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
