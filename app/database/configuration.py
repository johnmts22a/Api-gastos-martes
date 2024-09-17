
#Datos para la conexión a base de datos

dataBaseName = "gestordb"
userName = "root"
userPassword = ""
connectionPort = 3306
server = "localhost"

#Creando la conexión

dataBaseConnection = f"mysql+mysqlconnector://{userName}:{userPassword}@{server}:{connectionPort}/{dataBaseName}"

print(dataBaseConnection)