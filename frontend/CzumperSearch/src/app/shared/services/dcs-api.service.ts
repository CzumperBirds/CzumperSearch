import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DcsApiService {
  private baseUrl: string = 'https://api-test.czumpers.com/api/v1/data-collection'; // Replace with your API's base URL

  constructor(private http: HttpClient) {}

  getDCServiceStatus(): Observable<any> {
    const endpoint = `${this.baseUrl}/status`; // Replace with your endpoint
    console.log(endpoint)
    return this.http.get<any>(endpoint);
  }

  postData(body: any): Observable<any> {
    const endpoint = `${this.baseUrl}/control`; // Replace with your endpoint
    return this.http.post<any>(endpoint, body);
  }
}
