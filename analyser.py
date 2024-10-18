from typing import List, Tuple

class RouteAnalyzer:
    _routes:List[Tuple]


    def __init__(self) -> None:
        self._routes= []

    def __getitem__(self,idx):
        return self.routes[idx]

    @property
    def routes(self) -> List:
        return self._routes

    def __repr__(self) -> str:
        return f'RouteAnalyzer({self.routes})'


    def add_route(self,route:Tuple) -> None:
        match route:
            case [str(vehicle_type),(str(driver_name),int(driver_id)),[(str(dest),float(km)),*rest]]:
                self._routes.append(route)
            case _:
                raise ValueError(
                    f"""Invalid route : {route}. Expected [str(vehicle_type),(str(driver_name),int(driver_id)),[(str(destiny1),float(km1)),...]]"""
                )

    def analyze_route(self,route:Tuple) -> str:
        match route:
            case ["Truck",(str(driver_name),int(driver_id)),[*dests_and_kms]]:
                return f'Total distance for Truck: {sum( km for _,km in dests_and_kms)} km' 
            case ["Van",(str(driver_name),int(driver_id)),[*dests_and_kms]]:
                return f'Total destinations for Van: {len(dests_and_kms)}'
            case ["Motorcycle",(str(driver_name),int(driver_id)),[*dests_and_kms]]:
                return f'Driver {driver_name} is ready to deliver!'
            case [str(vehicle),*_]:
                return f"The vehicle type {vehicle} was not implemented yet!"
            case _:
                raise ValueError(
                    f"Invalid structure for route: {route}"
                )
            
if __name__=='__main__':
    # Criando uma instância da classe RouteAnalyzer
    analyzer = RouteAnalyzer()

    # Adicionando rotas
    analyzer.add_route(("Truck", ("Alice", 101), [("Berlin", 300.0), ("Hamburg", 150.0)]))
    analyzer.add_route(("Van", ("Bob", 202), [("Munich", 500.0)]))
    analyzer.add_route(("Motorcycle", ("Charlie", 303), [("Stuttgart", 75.0)]))
    analyzer.add_route(("Bicycle", ("Ben-Hur", 404), [("Chapada dos Guimarães", 25.0)]))

    # Analisando rotas
    for route in analyzer:
        result = analyzer.analyze_route(route)
        print(result)

    print(analyzer)


