import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {


  constructor(private http: HttpClient) { }

  uploadImage(formData: FormData) {
    return this.http.post<any>('http://127.0.0.1:5000/predict', formData); 
  }
}
