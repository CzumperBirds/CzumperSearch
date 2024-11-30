import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DcsApiService {
  private baseUrl: string = 'https://api-test.czumpers.com/api/v1/data-collection';

  constructor(private http: HttpClient) {}

  getDCServiceStatus(): Observable<any> {
    const endpoint = `${this.baseUrl}/status`;
    console.log(endpoint)
    return this.http.get<any>(endpoint);
  }

  postData(body: any): Observable<any> {
    const endpoint = `${this.baseUrl}/control`;
    return this.http.post<any>(endpoint, body);
  }
}
