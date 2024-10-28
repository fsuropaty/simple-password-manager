import random
import time

import click
import pyperclip

from utils.file_utils import pswd_to_file, read_pswd
from utils.generate_pass import generate_pass
from utils.strength_checker import result


@click.command()
def generate():
    click.echo("\n--- Password Generator ---")
    length = click.prompt("Enter the password length (>5)", type=int)

    if length <= 5:
        click.echo("Invalid password length")
        generate()

    uppercase = click.confirm("Do you want to include uppercase letter ?", default=True)
    lowercase = click.confirm("Do you want to include lowercase letter ?", default=True)
    numbers = click.confirm("Do you want to include numbers ?", default=True)
    symbols = click.confirm("Do you want to include symbols ?", default=True)

    generated_pass = generate_pass(length, uppercase, lowercase, numbers, symbols)

    print(f"\n{generated_pass}")

    click.echo("\nPlease select an option :")
    click.echo("\n1. Re-Generate password")
    click.echo("\n2. Copy password to clipboard")
    click.echo("\n3. Save the password")
    click.echo("\n4. Back to menu")
    click.echo("\n5. Quit")

    option = click.prompt("Please enter the number of your choice", type=int)

    match (option):
        case 1:
            generate()
        case 2:
            pyperclip.copy(generated_pass)
            click.echo("Your password has been copied to clipboard")
        case 3:
            name = click.prompt("\nPlease input the name for the password : ")
            pswd_to_file(name, generated_pass)
            click.echo("\nYour password has been saved")
            return
        case 4:
            main()
        case 5:
            return
        case _:
            print("Invalid option. Please try again")


@click.command()
def history():
    click.echo("\n--- Password History ---")
    read_pswd()


@click.command()
def strength():
    click.echo("\n--- Password Strength ---")
    pswrd = click.prompt("Enter your password", type=str)
    print(result(pswrd))

    ask = click.confirm("Do you want to quit?", default=True)
    if ask:
        return

    main()


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    random.seed(int(time.time()))

    if ctx.invoked_subcommand is None:
        click.echo("\nWelcome to Simple Password Manager")
        click.echo("----------------------------------")
        click.echo("Please select an option :")
        click.echo("1. Generate password")
        click.echo("2. Password history")
        click.echo("3. Check password strength")
        click.echo("----------------------------------")

        option = click.prompt("Please enter the number of your choice", type=int)

        match (option):
            case 1:
                ctx.invoke(generate)
            case 2:
                ctx.invoke(history)
            case 3:
                ctx.invoke(strength)
            case _:
                click.echo("Invalid option. Please try again")


main.add_command(generate)
main.add_command(history)
main.add_command(strength)


if __name__ == "__main__":
    main()
