class Company {
    constructor() {
        this.departments = [];
    }

    addEmployee(name, salary, position, department) {
        let inputData = [name, salary, position, department];

        for (const element of inputData) {
            if (element == '' || element == undefined || element == null || salary < 0) {
                throw Error('Invalid input!')
            }
        }

        if (this.departments[department] == undefined) {
            this.departments[department] = [];
        }

        this.departments[department].push({
            name,
            salary,
            position,
            department
        });

        return `New employee is hired. Name: ${name}. Position: ${position}`;
    }

    bestDepartment() {
        let department = '';
        let maxSalary = 0;

        Object.entries(this.departments).forEach(([key, value]) => {
            let salary = 0;
            value.forEach(e => {
                salary += e.salary;
            })
            salary = salary / value.length;
            if (salary > maxSalary) {
                department = key;
                maxSalary = salary;
            }
        });

        if (department != '') {
            let result = `Best Department is: ${department}\nAverage salary: ${maxSalary.toFixed(2)}\n`;
            Object.values(this.departments[department])
            .sort((a, b) => b.salary - a.salary || a.name.localeCompare(b.name)).forEach(e => {
                let em = `${e.name} ${e.salary} ${e.position}\n`;
                result += em;
            })
            return result.trim();
        }
    }
}

let c = new Company();
c.addEmployee("Stanimir", 2000, "engineer", "Construction");
c.addEmployee("Pesho", 1500, "electrical engineer", "Construction");
c.addEmployee("Slavi", 500, "dyer", "Construction");
c.addEmployee("Stan", 2000, "architect", "Construction");
c.addEmployee("Stanimir", 1200, "digital marketing manager", "Marketing");
c.addEmployee("Pesho", 1000, "graphical designer", "Marketing");
c.addEmployee("Gosho", 1350, "HR", "Human resources");
console.log(c.bestDepartment());

