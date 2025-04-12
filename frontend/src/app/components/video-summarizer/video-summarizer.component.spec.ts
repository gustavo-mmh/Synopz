import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VideoSummarizerComponent } from './video-summarizer.component';

describe('VideoSummarizerComponent', () => {
  let component: VideoSummarizerComponent;
  let fixture: ComponentFixture<VideoSummarizerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VideoSummarizerComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VideoSummarizerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
