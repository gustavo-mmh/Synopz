import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://127.0.0.1:5000'; // URL do backend Flask

  constructor(private http: HttpClient) {}

  getModels(apiKey: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/get_models`, { api_key: apiKey });
  }

  summarizeVideo(apiKey: string, modelName: string, youtubeUrl: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/`, {
      api_key: apiKey,
      model_name: modelName,
      youtube_url: youtubeUrl
    });
  }
}
