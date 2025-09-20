# Paso 1 Interactúa con el usuario para obtener entradas de información
user_prompt_input= input("Necesito comprar un vuelo ")

# Paso 2 Extraer los detalles del vuelo edl usuario como destino fecha y hora
prompt = [
  {"role": "system", "content": "Eres un asistente útil que extrae detalles de vuelos de las solicitudes de los usuarios."},
  {"role": "user", "content": user_prompt_input},
]
def fetch_flight_details():
  origen = "Madrid"
  destino = "Amsterdam"
  fecha = "2023-05-01"
  
  # Buscar opciones de vuelos en la base de datos de aerolíneas y terceros se organizan los resultados en una lista  
  def call_tool(tool_name, params):
    import requests
    if tool_name == "tool_uno":
      response = requests.post("https://api.example.com/flights", json=params)
      return {"flight": "123", "airline": "KLM", "departure": "10:00", "arrival": "12:00", "price": 150}
    elif tool_name == "tool_dos":
      response = requests.post("https://api.anotherexample.com/flights", json=params)
      return {"flight": "456", "airline": "Iberia", "departure": "11:00", "arrival": "13:00", "price": 140}
    elif tool_name == "tool_tres":
      response = requests.post("https://api.yetanotherexample.com/flights", json=params)
      return {"flight": "789", "airline": "Ryanair", "departure": "09:00", "arrival": "11:00", "price": 100}
    else:
      return None
  
  flight = []
  tool_uno = call_tool("tool_uno", {origen, destino, fecha})
  flight.append(tool_uno)
  
  tool_dos = call_tool("tool_dos", {origen, destino, fecha})
  flight.append(tool_dos)
  
  tool_tres = call_tool("tool_tres", {origen, destino, fecha})
  flight.append(tool_tres)
  
  return flight

def call_llm(messages):
  # Simula la llamada a un modelo de lenguaje (LLM)
  # Por ahora solo devuelve el último mensaje del usuario
  for msg in reversed(messages):
    if msg["role"] == "user":
      return msg["content"]
  return ""

def fetch_user_preferences():
  return

flight_query = call_llm(prompt)

# Paso 3 Buscar opciones de vuelos en la base de datos de aerolíneas y terceros
flight_options = fetch_flight_details()

# Paso 4 Buscar preferencias de usuario desde la memoria o bd
user_preferences = fetch_user_preferences()

# Paso 5 Preguntar al LLM con los detalles anteriores por las opciones de vuelos
decision_prompt = [
  {"role": "system", "content": f"User preferences: {user_preferences}"},
  {"role": "user", "content": f"Available flights: {flight_options}"},
]

decision = call_llm(decision_prompt)

# Paso 6 Lista de decisiones del usuario para reservar el vuelo en el sitio de reservas de la aerolínea o terceros
def book_flight(flight):
  return f"Flight {flight['flight']} on {flight['airline']} booked."

print (book_flight({"flight": "123", "airline": "KLM"}))

