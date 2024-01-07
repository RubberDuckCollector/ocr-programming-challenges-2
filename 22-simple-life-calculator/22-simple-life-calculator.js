function vat(price) {
    return `${price * 0.2} in tax`
}

function income_tax(salary) {
    
    if (salary <= 12570) {
        return "0% tax rate"
    } else if (salary >= 12571 && salary <= 50270) {
        return "20% tax rate"
    } else if (salary >= 50271 && salary <= 125140) {
        return "40% tax rate"
    } else {
        return "45% tax rate"
    }
}

function times_tables(num1, num2) {
    return num1 * num2
}

console.log(vat(452))

console.log(income_tax(12570))
console.log(income_tax(12571))
console.log(income_tax(125141))

console.log(times_tables(5, 4))
