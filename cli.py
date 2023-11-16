import click
from Final_project_pizza import Pizza, Pepperoni, Hawaiian, Margherita
from timer import time_check


names_of_pizza = ["margherita", "pepperoni", "hawaiian"]


@time_check("👨‍🍳 Приготовили за {}с!")
def bake(pizza: Pizza):
    """
    Prepare pizza.

    :param pizza: The pizza to bake.
    """
    # Logic for baking pizza


@time_check("🛵 Доставили за {}с!")
def delivery(pizza: Pizza):
    """
    Deliver pizza.

    :param pizza: The pizza to deliver.
    """
    # Logic for pizza delivery


@time_check("🏠 Забрали за {}с!")
def pickup(pizza: Pizza):
    """
    Self pickup.

    :param pizza: The pizza for self pickup.
    """
    # Logic for pizza pickup


@click.group()
def cli():
    """
    Interface for pizza ordering
    """


@cli.command()
@click.option("--delivery",
              "need_delivery",
              default=False,
              is_flag=True,
              help="Include this option for delivery")
@click.option("--size", default="XL", help="You can choose your pizza size.")
@click.argument("pizza", nargs=1)
def order(pizza: str, size: str, need_delivery: bool):
    """
    Prepare and deliver pizza.

    :param pizza: The type of pizza to order.
    :param size: The size of pizza to order.
    :param need_delivery: Flag indicating whether the delivery is needed.
    """
    pizza_obj = None
    if pizza not in names_of_pizza:
        print("Sorry. We do not have such type of pizza :(")
        return None
    elif pizza == "Margherita":
        pizza_obj = Margherita(size)
    elif pizza == "Pepperoni":
        pizza_obj = Pepperoni(size)
    elif pizza == "Hawaiian":
        pizza_obj = Hawaiian(size)
    bake(pizza_obj)
    if need_delivery:
        delivery(pizza_obj)
    else:
        print("Enjoy your pizza. Bon appetit!")


@cli.command()
def menu():
    """Display the menu."""
    margherita = Margherita()
    pepperoni = Pepperoni()
    hawaiian = Hawaiian()
    margherita_ingredients = ", ".join(margherita.ingredients)
    pepperoni_ingredients = ", ".join(pepperoni .ingredients)
    hawaiian_ingredients = ", ".join(hawaiian.ingredients)
    click.echo(f"- {margherita.name} 🧀 : {margherita_ingredients}")
    click.echo(f"- {pepperoni.name} 🍕 : {pepperoni_ingredients}")
    click.echo(f"- {hawaiian.name} 🍍 : {hawaiian_ingredients}")


if __name__ == "__main__":
    cli()
