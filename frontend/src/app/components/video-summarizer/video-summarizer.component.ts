import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { NgbPaginationModule } from '@ng-bootstrap/ng-bootstrap';
import { AlertComponent } from '../alert/alert.component';
import { LoadingComponent } from '../loading/loading.component';
@Component({
  selector: 'app-video-summarizer',
  templateUrl: './video-summarizer.component.html',
  styleUrls: ['./video-summarizer.component.scss'],
  standalone: true, // Define que este componente é um componente independente (standalone)
  imports: [AlertComponent, CommonModule, FormsModule, NgbPaginationModule, LoadingComponent] // Importa os módulos necessários
})
export class VideoSummarizerComponent {
  apiKey: string = '';
  alertType: 'success' | 'error' = 'success';
  alertMessage: string = '';
  isVisible: boolean = false;
  videoUrl: string = '';
  youtubeUrl: string = '';
  selectedModel: string = '';
  models: string[] = [];
  thumbnailUrl: string | null = null;
  isApiValid: boolean = false;
  isLoading: boolean = false;
  isLoadingModel: boolean = false;
  summary: string | null = null;
  errorMessage: string | null = null;

  constructor(private apiService: ApiService) { }

  validateApiKey() {
    this.isVisible = false; // Redefine a visibilidade do alerta
    this.apiService.getModels(this.apiKey).subscribe(
      (response) => {
        this.models = response.models;
        this.isVisible = true;
        this.isApiValid = true;
        this.alertType = 'success';
        this.alertMessage = 'Api Conectada com sucesso!';
        this.isLoadingModel = false;
      },
      (error) => {
        console.log(error);
        this.isVisible = true;
        this.isApiValid = false;
        this.isLoadingModel = false;
        this.alertType = 'error';
        this.alertMessage = 'Api Inválida!';
      }
    );
  }
  loadThumbnail() {
    const videoId = this.extractVideoId(this.youtubeUrl);
    if (videoId) {
      this.thumbnailUrl = `https://img.youtube.com/vi/${videoId}/0.jpg`;
    } else {
      this.thumbnailUrl = '';

    }
  }
  extractVideoId(videoUrl: string): string | null {
    const match = videoUrl.match(/(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([^&]+)/);
    return match ? match[1] : null;
  }
  loadModels() {
    this.apiService.getModels(this.apiKey).subscribe({
      next: (response) => {
        this.models = response.models;
      },
      error: (error) => {
        this.alertMessage = 'Erro ao carregar modelos.';
        this.alertType = 'error';
        this.isVisible = true;
      },
      complete: () => {
        this.alertMessage = 'modelos carregados com sucesso.';
        this.alertType = 'success';
        this.isVisible = true;
       }
    });
  }

  summarize() {
    this.summary = null;
    this.apiService.summarizeVideo(this.apiKey, this.selectedModel, this.youtubeUrl).subscribe(
      {
        next: (response) => {
          this.isLoading = true;
          this.summary = response.summary;

        },
        error: (error) => {
          this.isVisible = true;
          this.alertType = 'error';
          this.alertMessage = 'Erro ao gerar resumo.';
          console.error(error);
        },
        complete: () => {
          this.alertType = 'success';
          this.alertMessage = 'resumo gerado com sucesso.';
          this.isVisible = true;
          this.isLoading = false;
        }
      }
    );
  }

  copySummary() {
    if (this.summary) {
      navigator.clipboard.writeText(this.summary).then(() => {
        alert('Resumo copiado para a área de transferência!');
      }, (err) => {
        console.error('Erro ao copiar o resumo: ', err);
      });
    }
  }

  exportToDoc() {
    if (this.summary) {
      const blob = new Blob([this.summary], { type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' });
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'resumo.doc';
      a.click();
      window.URL.revokeObjectURL(url);
    }
  }
}
