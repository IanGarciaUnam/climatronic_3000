package mx.forecast;

import java.net.Socket;

/***
*@(#)NetConnection.java
*La utilidad de esta clase radica en simplemente verificar
*que se cuente con una conexión adecuada a Internet, pues de ahí partirán
*las decisiones para utilizar o no la caché mientras se espera que esta logre 
*obtenerse
*
*@author Ian Garcia
*@version 1.00 2020/09/26
*
*/
public class NetConnection{

	NetConnection(){};//COnstructor vacío


	/**Comprueba la conexión a internet de forma General
	*
	*@return true| false Hay o no hay conexión a internet
	*/

	public static boolean hasConnection(){
		return comprobador("www.google.com", 80);
	}


	/**
	*Comprueba la conexión a internet 
	*con un sitio en especifico
	*@param website String del website
	*@return true|false
	*/
	public boolean hasConnectionTo(String website){
		return comprobador(website,80);
	}	


	private static boolean comprobador(String website, int puerto){
		String web=website; // Puede utilizarse una página web arbitraria
		try{
			Socket s = new Socket(web, 80); // Utilizamos el perto 80 por convención
			if(s.isConnected())
				return true;
		}catch(Exception e){
			return false;
		}
		return true;
	}


}