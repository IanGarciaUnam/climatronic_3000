package mx.forecast;



public class Climatronic{

	public static void main(String[] args){
		System.out.println("Deux xposito");

		/**
		*Comprobando funcionamiento de la conexión a internet
		*
		*/
		System.out.println("General Test "+ NetConnection.hasConnection());
		NetConnection n = new NetConnection();
		System.out.println("Testing openWeather "+ n.hasConnectionTo("openweather.org"));
	}




}