import click
import json_manager

@click.group()
def cli():
    pass

@cli.command()
@click.option('--nombre', required=True, help='Nombre del usuario')
@click.option('--apellido', required=True, help='Apellido del usuario')
@click.pass_context
def new(ctx, nombre, apellido):
    if not nombre or not apellido:
        ctx.fail('nombre y apellido requeridos !!!')
    else:
        data=json_manager.read_json()  
        next_id = len(data) + 1
        next_user = {
            'id':next_id,
            'nombre':nombre,
            'apellido':apellido
        }
        data.append(next_user)
        json_manager.write_json(data)
        print(f"Usuario {nombre} {apellido} creado exitosamente !!! con id {next_id}")

@cli.command()
def users():
    users = json_manager.read_json()
    for user in users:
        print(f"{user['id']} - {user['nombre']} - {user['apellido']}")


if __name__ == '__main__':
    cli()

