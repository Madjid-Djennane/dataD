import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class TraficService {

  constructor(private http: HttpClient) { }


  private uri = 'http://127.0.0.1:5000/';

  getIps() {
    return this.http.get(this.uri + 'ips');
  }


  getHits(date1, date2) {
    return this.http.get(this.uri + 'httpHits/' + date1 + '/' + date2);
  }
}
