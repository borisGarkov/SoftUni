movie_name = input()
total_tickets = 0
grand_total_tickets = 0
grand_total_student = 0
grand_total_standard = 0
grand_total_kid = 0
while movie_name != "Finish":

    free_seats = int(input())

    standard_ticket = 0
    student_ticket = 0
    kid_ticket = 0

    while total_tickets < free_seats:
        ticket_type = input()

        if ticket_type == "standard":
            standard_ticket += 1
        elif ticket_type == "student":
            student_ticket += 1
        elif ticket_type == "kid":
            kid_ticket += 1

        if ticket_type == "End":
            break

        total_tickets = standard_ticket + student_ticket + kid_ticket

    print(f"{movie_name} - {(total_tickets / free_seats) * 100:.2f}% full.")

    grand_total_tickets += total_tickets
    grand_total_student += student_ticket
    grand_total_standard += standard_ticket
    grand_total_kid += kid_ticket

    total_tickets = 0
    movie_name = input()

print(f"Total tickets: {grand_total_tickets}\n{(grand_total_student / grand_total_tickets) * 100:.2f}% student tickets.")
print(f"{(grand_total_standard / grand_total_tickets) * 100:.2f}% standard tickets.")
print(f"{(grand_total_kid / grand_total_tickets) * 100:.2f}% kids tickets.")