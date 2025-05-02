import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { NgbPaginationModule } from '@ng-bootstrap/ng-bootstrap';
import { AlertComponent } from '../alert/alert.component';
import { LoadingComponent } from '../loading/loading.component';
import { LucideAngularModule, FileIcon, PlayCircle } from 'lucide-angular';
import { LucideIconsModule } from '../../modules/lucide-icons/lucide-icons.module';
@Component({
  selector: 'app-video-summarizer',
  templateUrl: './video-summarizer.component.html',
  styleUrls: ['./video-summarizer.component.scss'],
  standalone: true, // Define que este componente é um componente independente (standalone)
  imports: [AlertComponent, CommonModule, FormsModule,
    NgbPaginationModule, LoadingComponent, LucideAngularModule, LucideIconsModule ] // Importa os módulos necessários
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
  readonly FileIcon = FileIcon;
  readonly PlayCircle = PlayCircle;
  constructor(private apiService: ApiService) { }
  
  validateApiKey() {
    if (this.apiKey !== "") {
    this.isLoadingModel = true
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
          this.alertMessage = this.formatApiError(error)  || 'Erro ao gerar resumo.';
          this.isLoading = false;
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
        this.isVisible = true
        this.alertMessage = 'Resumo copiado para a área de transferência!';
      }, (err) => {
        this.isVisible = true
        this.alertMessage = 'Erro ao copiar o resumo:';
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
      this.isVisible = true
      this.alertMessage = 'Documento exportado com sucesso!';
    }
  }
  formatApiError(error: any): string {
    const message = error?.error?.error || 'Erro desconhecido';

    if (message.includes('Video unavailable') || message.includes('Vídeo indisponível')) {
      return 'Este vídeo está indisponível ou não possui legendas públicas.';
    }

    if (message.includes('Não foi possível baixar a legenda')) {
      return 'Não conseguimos acessar a legenda deste vídeo. Tente outro.';
    }

    if (message.includes('API Key não fornecida')) {
      return 'Por favor, informe sua chave de API Gemini.';
    }

    if (message.includes('Modelo não selecionado')) {
      return 'Selecione um modelo antes de gerar o resumo.';
    }

    return 'Ocorreu um erro ao processar o vídeo. Verifique os dados e tente novamente.';
  }

}
