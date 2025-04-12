import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-video-summarizer',
  templateUrl: './video-summarizer.component.html',
  styleUrls: ['./video-summarizer.component.scss'],
  standalone: true, // Define que este componente é um componente independente (standalone)
  imports: [CommonModule, FormsModule] // Importa os módulos necessários
})
export class VideoSummarizerComponent {
  apiKey = '';
  youtubeUrl = '';
  selectedModel = '';
  models: string[] = [];
  thumbnailUrl = '';
  isApiValid = false;
  isLoading = false;
  summary = '';
  error = '';

  constructor(private apiService: ApiService) {}

  validateApiKey() {
    this.apiService.getModels(this.apiKey).subscribe(
      (response) => {
        this.models = response.models;
        this.isApiValid = true;
        alert('API válida!');
      },
      (error) => {
        this.isApiValid = false;
        // alert('API inválida!');
      }
    );
  }
  loadThumbnail() {
    const videoId = this.extractVideoId(this.youtubeUrl);
    if (videoId) {
      this.thumbnailUrl = `https://img.youtube.com/vi/${videoId}/0.jpg`;
    } else {
      this.thumbnailUrl = '';
      // alert('URL do YouTube inválida!');
    }
  }
  extractVideoId(url: string): string | null {
    const match = url.match(/(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([^&]+)/);
    return match ? match[1] : null;
  }
  loadModels() {
    this.apiService.getModels(this.apiKey).subscribe(
      (response) => {
        this.models = response.models;
      },
      (error) => {
        this.error = 'Erro ao carregar modelos.';
        console.error(error);
      }
    );
  }

  summarize() {
    this.apiService.summarizeVideo(this.apiKey, this.selectedModel, this.youtubeUrl).subscribe(
      (response) => {
        this.summary = response.summary;
      },
      (error) => {
        this.error = 'Erro ao gerar resumo.';
        console.error(error);
      }
    );
  }
}
