import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment.prod';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = environment.apiUrl;

  constructor(private http: HttpClient) { }

  getModels(apiKey: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/get_models`, { api_key: apiKey });
  }

  summarizeVideo(apiKey: string, modelName: string, youtubeUrl: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/summarize`, {
      api_key: apiKey,
      model_name: modelName,
      youtube_url: youtubeUrl
    });
  }
}
