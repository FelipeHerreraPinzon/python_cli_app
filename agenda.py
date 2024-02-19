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


@cli.command()
@click.argument('id', type=int)
@click.option('--nombre', help='Nombre del usuario')
@click.option('--apellido', help='Apellido del usuario')
def update(id, nombre, apellido):
    users = json_manager.read_json()
    for user in users:
        if user['id'] == id:
            if nombre is not None:
                user['nombre'] = nombre
            if apellido is not None:
                user['apellido'] = apellido
            break    
    json_manager.write_json(users)    
    print(f"User with id {id} updated successfully")


@cli.command()
@click.argument('id', type=int)
def user(id):
    users = json_manager.read_json()
    user = next((user for user in users if user['id'] == id), None)
    if user is None:
        print(f"User with id {id} not found")
    else:    
        print(f"{user['id']} - {user['nombre']} - {user['apellido']}")


@cli.command()
@click.argument('id', type=int)
def delete(id):
    users = json_manager.read_json()
    userDelete = next((user for user in users if user['id'] == id), None)
    if userDelete is None:
        print(f"User with id {id} not found")
    else:    
        users.remove(userDelete)
        json_manager.write_json(users)
        print(f"User with id {id} was deleted")


if __name__ == '__main__':
    cli()

