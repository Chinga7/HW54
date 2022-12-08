from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.utils.http import urlencode

from webapp.models import Issue, Project
from django.views.generic import View, FormView, ListView, DetailView, CreateView
from webapp.forms import IssueForm, SearchForm
from webapp.views.base_views import CustomFormView, CustomSearchView


class IssueListView(ListView):
    template_name = 'issues/issue_list.html'
    model = Issue
    context_object_name = 'issues'
    ordering = ('-created_at')
    paginate_by = 3
    paginate_orphans = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = SearchForm
        return context


class SearchView(CustomSearchView):

    template_name = 'issues/project_list.html'
    model = Issue
    search_form = SearchForm
    context_object_name = 'issues'
    ordering = ('-created_at')
    paginate_by = 3
    paginate_orphans = 2

    def get_queryset(self):
        if self.search_value:
            queryset = super().get_queryset()
            queryset = queryset.filter(Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search'] = self.search_value
        return context


class IssueView(DetailView):
    template_name = 'issues/issue.html'
    model = Issue


class CreateIssueView(CreateView):
    template_name = "issues/create.html"
    model = Issue
    form_class = IssueForm

    # def get_success_url(self):
    #     return reverse('issue_detail', kwargs={'pk': self.object.issue.pk})

    def form_valid(self, form):
        project = (get_object_or_404(Project, pk=self.kwargs.get('pk')))
        issue = form.save(commit=False)
        issue.project = project
        issue.save()
        return redirect('project_detail', pk=project.pk)


class UpdateView(FormView):
    template_name = "issues/update.html"
    form_class = IssueForm

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Issue, pk=pk)

    def dispatch(self, request, *args, **kwargs):
        self.issue = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = self.issue
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.issue
        return kwargs

    def form_valid(self, form):
        self.issue = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'pk': self.issue.pk})


class DeleteView(View):
    def get(self, request, pk):
        issue = get_object_or_404(Issue, pk=pk)
        context = {'issue': issue}
        return render(request, 'issues/delete.html', context)

    def post(self, request, pk):
        issue = get_object_or_404(Issue, pk=pk)
        issue.delete()
        return redirect('project_list')