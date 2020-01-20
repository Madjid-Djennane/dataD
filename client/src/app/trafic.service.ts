import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class TraficService {

  constructor(private http: HttpClient) { }


  private uri = 'http://127.0.0.1:5000/';

  // retourne la liste des ip's triées par ordre décroissant de hits http
  getIps() {
    return this.http.get(this.uri + 'ips');
  }

  // retourne une vue du trafic selon une fenêtre de temps
  getTrafic(date1, date2) {
    return this.http.get(this.uri + 'trafic/' + date1 + '/' + date2);
  }
}
